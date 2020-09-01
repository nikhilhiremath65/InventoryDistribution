#!/usr/bin/python
# ##############################################Module Information################################################
#  Module Name         :   Inventory Distribution
#  Purpose             :   Finds the best way an order can be shipped  given inventory across a set of warehouses
#  Input Parameters    :   Order Details and Inventory Details across multiple warehouses
#  Output Value        :   Empty array if order can not be full filled OR
#                          A list of warehouses from where order can be full filled
#  Pre-requisites      :   None
#  Last changed on     :   Aug 31, 2020
#  Last changed by     :   Nikhil Hiremath
#  Reason for change   :   Added loggers to the Program
# ################################################################################################################


import logging
import CommonConstants
__AUTHOR__ = 'Nikhil Hiremath'


class InventoryDistribution:

    def check_inventory(self,item, orderDetails, inventoryDetails):
        try:
            temp = []
            for inventory in inventoryDetails:
                logging.info("Current Inventory = "+ str(inventory))
                # Check if item is available in the inventory
                if item not in inventory["inventory"]:
                    logging.info("Element " + item + " is not available in " + inventory["name"])

                # check if item quantity is sufficient and add to temp
                elif orderDetails[item] <= inventory["inventory"][item]:
                    orderDetails[item] = orderDetails[item] - inventory["inventory"][item]
                    temp.append(inventory)
                else:
                    orderDetails[item] = orderDetails[item] - inventory["inventory"][item]
                    temp.append(inventory)
            return temp
        except Exception as exception:
            status_message = "Order shipment program failed due to" + str(exception)
            logging.debug(status_message)
            # logging.info()

    def process_items(self, orderDetails, inventoryDetails):
        try:
            self.result=[]
            # Iterate across each item in the orderDetails
            for item in orderDetails:
                logging.info("Current Item = " + item)
                
                # Iterating each inventory across a set of warehouses
                logging.info("inventoryDetails = " + str(inventoryDetails))
                warehouse = self.check_inventory(item, orderDetails, inventoryDetails)
                logging.info("warehouse: "+ str(warehouse))
                if orderDetails[item] <= 0:
                    self.result.append(warehouse)
                else:
                    logging.info("Item " + item + " quantity is not sufficient")
                print("result= ", self.result)
        except Exception as exception:
            status_message = "ERROR: InventoryDistribution: Exception Occurred  " + str(exception)
            logging.debug(status_message)

    def main(self):
        # Configuring the Logger
        logging.basicConfig(filename=CommonConstants.LOG_FILE,level=logging.INFO)
        logging.info('Started')
        # Test Cases
        self.process_items({"apple": 1}, [{"name": "owd", "inventory": {"apple": 1}}])
        self.process_items({"apple": 2}, [{"name": "owd", "inventory": {"apple": 0}}])
        self.process_items({"apple": 2}, [{"name": "owd", "inventory": {"apple": 1}}])
        self.process_items({"mango": 4}, [{"name": "owd", "inventory": {"mango": 15}}])
        self.process_items({"apple":8 },[{"name": "owd", "inventory": {"apple": 5}},
                                          {"name": "dm", "inventory": {"apple": 5}}])
        self.process_items({"apple": 10}, [{"name": "owd", "inventory": {"apple": 5}},
                                          {"name": "dm", "inventory": {"apple": 5}}])

        logging.info('Finished')


if __name__ == '__main__':
    a = InventoryDistribution()
    a.main()



