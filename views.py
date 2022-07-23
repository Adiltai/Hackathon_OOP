import json

class Cars():

    id=0
    like = 0
    comment=None
    FILE='jsondb/data.json'
    typeModel = ("sedan", "universal", "cupe", "hatchback", "minivan", "jeep", "pickup")
    def __init__(self,marka,model,year,volume_of_engine,color,typeModel,mileage,price):
        self.marka=marka
        self.model=model
        self.year=year
        self.volume_of_engine=volume_of_engine
        self.color=color
        self.mileage=mileage
        self.price=price
        if typeModel in Cars.typeModel:
            self.typeModel = typeModel
        else:
            raise Exception("Car 'body type' is not valid")
        self.send_car_to_json()

    @classmethod
    def get_car_id(cls):
        cls.id+=1
        return cls.id

    @classmethod
    def listing(cls):
        with open(cls.FILE) as file:
            return json.load(file)
    
    @staticmethod
    def get_one_car(data,id):
        machine=list(filter(lambda x:x['id']==id,data))
        if not machine:
            return 'There is no such a machine'
        return machine[0]

    @classmethod
    def send_data_to_json(cls,data):
        with open(cls.FILE,'w') as file:
            json.dump(data,file)

    def send_car_to_json(self):
        data=Cars.listing()
        machine={
            'id':Cars.get_car_id(),
            'marka':self.marka,
            'model':self.model, 
            'year':self.year, 
            'volume_of_engine':self.volume_of_engine, 
            'color':self.color, 
            'typeModel':self.typeModel, 
            'mileage':self.mileage, 
            'price':self.price,
            'like':Cars.like,
            'comment': Cars.comment
            }
        data.append(machine)
        
        with open(Cars.FILE,'w') as file:
            json.dump(data,file)
        return {'status':'201','msg':machine}

    @classmethod
    def retrieve_data(cls,id):
        data=cls.listing()
        machine=cls.get_one_car(data,id)
        return machine

    @classmethod
    def delete_data(cls,id):
        data=cls.listing()
        machine=cls.get_one_car(data,id)
        if type(machine)!=dict:
            return machine

        index=data.index(machine)
        data.pop(index)
        cls.send_data_to_json(data)
        return{'status':'204','msg':'Deleted'}


    @classmethod
    def update_data(cls,id, **kwargs):
        data=cls.listing()
        machine = cls.get_one_car(data,id)
        index = data.index(machine)
        data[index].update(**kwargs)
        cls.send_data_to_json(data)
        return{'status':'200','msg':'Updated'}
    
    @classmethod
    def like_(cls, id):
        try:
            data = cls.listing()
            if data[id - 1]['like'] == 0:
                data[id - 1]['like'] += 1
                print('liked')
            else:
                data[id - 1]['like'] -= 1
                print('unliked')
            cls.send_data_to_json(data)
        except IndexError:
            print('Нет такого автомобиля')
   

    @classmethod
    def comments(cls,id, **kwargs ):
        data=cls.listing()
        machine = cls.get_one_car(data,id)
        index = data.index(machine)
        data[index].update(**kwargs)
        cls.send_data_to_json(data)
        return{'status':'200','msg':'commented'}