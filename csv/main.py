import csv







def main():
    orders = {}
    productsdic = {}
    proprice = {}
    custmer_products = {}
    productIdPrice = {}
    customerName = {}
    customerTotalMoney = {}
    print('----------------Customers----------------------')
    with open('customers.csv',newline='') as csv_file:
        readerCustomer = csv.reader(csv_file,skipinitialspace=True)
        next(readerCustomer)
        for line in readerCustomer:
            id = int(line[0])
            name = line[1]
            address = line[2]
            customerName[id] = name
            print(f'Customer: {name}, {address}')
    print('-----------------Products--------------------------')
    with open('products.csv',newline='') as csv_file:
        readerProducts = csv.reader(csv_file,skipinitialspace=True)
        next(readerProducts)
        for line in readerProducts:
            pid = int(line[0])
            pname = line[1]
            price = int(line[2])
            productsdic[pid] = pname
            proprice[pname] = price
            productIdPrice[pid] = price
            print(f'Product: {pname}, {price}')

    print('--------------------Orders------------------------------')
    readerOrders = csv.reader(open('orders.csv'))

    next(readerOrders)
    for line in readerOrders:
        cid = int(line[1])
        prid = int(line[2])
        amount = int(line[3])
        if prid in orders.keys():
            orders[prid] += amount
        else:
            orders[prid] = amount

    res_orders = {}
    for k in orders.keys():
        name = productsdic[k]
        amount = orders[k]
        res_orders[name] = amount
    for k,v in res_orders.items():
        print(f'{k} amount: {v}')
    print('-----------------------------------------------------')
    products_totlal_price = {}
    for k in res_orders.keys():
        price = proprice[k]
        amount = res_orders[k]
        total = price * amount
        products_totlal_price[k] = total
        print(f'{k} gross income: {total}')
    print('---------------------------------------------------------')
    with open('orders.csv',newline='') as csv_file:
        readerOrders = csv.reader(csv_file,skipinitialspace=True)
        next(readerOrders)

        for line in readerOrders:
            cid = int(line[1])
            prid = int(line[2])
            amount = int(line[3])
            if cid in custmer_products.keys():
                value = custmer_products[cid]
                if prid in value.keys():
                    value[prid] += amount
                else:
                    value[prid] = amount
            else:
                custmer_products[cid] = {prid:amount}
    print('---------------------------------------------------------')
    print(custmer_products)
    print('---------------------------------------------------------')
    for cId in custmer_products.keys():
        cName = customerName[cId]
        cProdAmount = custmer_products[cId]
        cTotal = 0
        for pId in cProdAmount.keys():
            pAmount = cProdAmount[pId]
            pPrice = productIdPrice[pId]
            cTotal += (pAmount * pPrice)
        customerTotalMoney[cName] = cTotal
    for k,v in customerTotalMoney.items():
        print(f'{k} money spent: {v}')

    print('---------------------------------------------------------')



if __name__ == '__main__':
    main()
