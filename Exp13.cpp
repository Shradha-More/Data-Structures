#include <iostream>
#include <malloc.h>
using namespace std;

class Test {
public:
    int SIZE, MyQueue[3], front, rear, element;

    Test() {
        SIZE = 3;
        front = -1;
        rear = -1;
    }
    void enQueue() {
        if ((front==0&&rear==SIZE-1) || (front==rear+1)) 
        {
            cout << "\nPizza Booking is full!!\n";
        } 
        else {
            cout << "\nEnter Pizza Quantity: ";
            cin >> element;
            if (rear == SIZE - 1 && front != 0)
            {
            rear = -1;
            }
            MyQueue[++rear] = element;
            if (front == -1) {
                front = 0;
            }
        }
    }
    void deQueue() {
        if (front == -1 && rear == -1) {
            cout << "\nPizza can't be served due to unavailability!!!\n";
        } 
        else {
            cout << "\nPizza served: " << MyQueue[front++];
            if (front == SIZE)
            {
                front = 0;
            }
            if (front == rear + 1)
            {
                front = rear = -1;
            }
        }
    }
    void display() {
        if (front == -1)
        {
            cout << "\n out of pizza!!!\n";
        } 
        else {
            int i = front;
            cout << "\nPizzas ordered are:\n";
            if (front <= rear)
            {
                while (i <= rear) 
                {
                    cout << "\t" << MyQueue[i++] << "\n";
                }
            } 
            else {
                while (i <= rear) 
                {
                    cout << "\t" << MyQueue[i++] << "\n";
                }
            }
        }
    }
};

int main() {
    Test obj;
    int choice;
    while (1)
    {
        cout << "\n************Welcome to Pizza Hut************\n";
        cout << "\n1. Place an order\n2. Serve a pizza\n3. Display Remaining orders\n4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;
        switch (choice)
        {
            case 1:
                obj.enQueue();
                break;
            case 2:
                obj.deQueue();
                break;
            case 3:
                obj.display();
                break;
            case 4:
                cout << "Exiting...\n";
                break;
            default:
                cout << "Invalid choice!\n";
                break;
        }
    }
return 0;
}