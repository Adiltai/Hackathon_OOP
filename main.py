from views import Cars


def main():
    print('1)Create a new car\n2)Get list of cars\n3)Retrieve data about one car\n4)Update car\n5)Delete car\n6)Do you want like some cars\n7)Do you want comment some cars\n8)Exit')
    a=int(input('Выберите действие:'))
    if a == 1:
        brand=input('Brand:')
        model=input('Model:')
        year=int(input('Year of issue:'))
        volume=float(input('Engine volume:'))
        color=input('Color:')
        body=(input('Body: '))
        mileage=int(input('Milage:'))
        price=float(input('Price:'))
        Cars(brand, model, year, volume,color, body, mileage, price).send_car_to_json
        q=input('do u want to continue?(1-yes,2-no)')
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye!')
        else:
            print('Error')
            main()
    elif a==2:
        print(Cars.listing())
        q=int(input('do u want to continue?(1-yes,2-no)'))
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye!')
        else:
            print('Error')
            main()

    elif a==3:
        object=int(input('Enter object index:'))
        print(Cars.retrieve_data(object))
        q=int(input('do u want to continue?(1-yes,2-no)'))
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye!')
        else:
            print('Error')
            main()
        
    elif a==4:
        id=int(input('Enter object index:'))
        kwargs = {}
        obj = input('What do you want to change?')
        val = input('What value do you want to change: ')
        kwargs[obj] = val
        print(Cars.update_data(id, **kwargs))
        q=int(input('do u want to continue?(1-yes,2-no)'))
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye!')
        else:
            print('Error')
            main()
        
    elif a==5:
        id=int(input('Enter object index:'))
        print(Cars.delete_data(id))
        q=int(input('do u want continue?(1-yes,2-no)'))
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye!')
        else:
            print('Error')
            main()
    elif a == 6:
        id = int(input('Enter object index:'))
        print(Cars.like_(id))
        q=int(input('do u want to continue?(1-yes,2-no)'))
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye!')
        else:
            print('Error')
            main()
    elif a==7:
        id=int(input('Enter object index:'))
        kwargs = {}

        com = input('What coment do you want to add: ')
        kwargs['comment'] = com
        print(Cars.comments(id, **kwargs))
        q=int(input('do u want continue?(1-yes,2-no)'))
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye!')
        else:
            print('Error')
            main()

    elif a == 8:
        print('Okay bye!')
        
    else:
        print('Error')
        q=int(input('do u want continue?(1-yes,2-no)'))
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye!')
        else:
            print('Error')
            main()
        
    


main()