

from datetime import*
from Stock_Report import Stock


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.top = None
        self.size = 100
        self.cnt = 0

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            temp = Node(data)
            self.tail.next = temp
            self.tail = temp

    def search(self, data):
        if self.head.data['StockName'] == data:
            return True
        else:
            return False

    def delete(self, data):
        if self.head.data['StockName'] == data:
            self.head = self.head.next
        else:
            prev = None
            temp = self.head
            while temp is not None:
                if temp.data['StockName'] == data:
                    prev.next = temp.next
                prev = temp
                temp = temp.next

    def print_rep(self):
        if self.head is not None:
            dt, tm = self.date_time()
            temp = self.head
            print("{:<15} {:<15} {:<15} {:<15} {:<24}".format("Name", "Qty", "Price", "Total Value", "Time & Date"))
            while temp is not None:
                print("{:<15} {:<15} {:<15} {:<15} {:<16} {:<8}".format(temp['StockName'], temp['Shares']
                        , temp['StockPrice'], temp['StockPrice'] * temp['Shares'], dt, tm))
                temp = temp.next

        else:
            print("List is Empty")

    @staticmethod
    def date_time():
        d = date.today()
        t = datetime.now()
        tm = t.strftime("%H:%M:%S")
        dt = d.strftime("%b %d, %Y")
        return dt, tm

    # *******************************  Method insert element at the Top  *****************************

    def push(self, data):
        if self.top is None:  # Check if stack is Empty and if found empty
            self.top = Node(data)  # Add element at the Top
            self.cnt += 1
        else:  # Else add the element before Top and Update top to Newly added element.
            temp = Node(data)
            temp.next = self.top
            self.top = temp
            self.cnt += 1

    def get_item(self, name):
        temp = self.top
        while temp is not None:
            if temp['StackName'] == name:
                return temp
            temp = temp.next

    # ***************************  Method give top element and remove it. *********************

    def pop(self):
        val = self.top.data
        self.top = self.top.next
        self.cnt -= 1
        return val

    # **********************************  Method checks if Stack is Empty or not  ***********************

    def is_empty(self):
        if self.top is None:
            return True  # Returns True if Found Empty.
        else:
            return False  # Return False if not found empty.
    # ********************************  Method to check if stack become Full or not  ************************

    def is_full(self):
        if self.cnt == self.size:
            return True
        else:
            return False

    def stack_size(self):
        return self.cnt

    def peek(self):
        return self.top.data  # Return Top element

    def print_stack(self):
        if self.top is None:
            print('Stack is Empty.\nNo Transaction History found.')
        else:
            temp = self.top
            while temp is not None:
                for i in temp:
                    st = temp[i]
                    print(i, ':', st)
                temp = temp.next
