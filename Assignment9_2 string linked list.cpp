//Second year Computer Engineering class, set A of students like Vanilla Ice-cream and set 
// B of students like butterscotch ice-cream. Write C++ program to store two sets using 
//linked list. compute and display
//a) Set of students who like both vanilla and butterscotch
//b) Set of students who like either vanilla or butterscotch or not both
//c) Number of students who like neither vanilla nor butterscotch


#include<iostream>
#include<vector>
using namespace std;

class node{
	public:
		string name;
		char van,but;
		node *next;
		node(){
			next = nullptr;
		}
};
class List
{
	node *head;
	public:
		List()
		{
			head = NULL;
		}
	
		void insertAtEnd(string s,char v,char b)
		
		{
			node *p = new node();
			p->van = v;
			p->name=s;
			p->but=b;
			if (head == NULL)
			{
				head = p;
			}
			else
			{
				
				node *ptr = head;
				while (ptr->next != NULL)
				{
					ptr = ptr->next;
				}
				ptr->next = p;
			}
		}
		
		void display()
		{
			int count=0;
			if (head == NULL){
				cout<<"List is empty"<<endl;
			}
			else
			{
				
				node *p = head;
				cout<<"Linked List: \n";
				while (p != NULL){
					cout<<p->name<<"\t"<<p->van<<"\t"<<p->but<<"\n";
					count++;
					p = p->next;
				}
			
			}
			cout<<"Number of elemnets in linked list:"<<count;
		}	
		void disp_vanAndbut()
		{
			//int count=0;
			if (head == NULL){
				cout<<"List is empty"<<endl;
			}
			else
			{
				
				node *p = head;
				cout<<"students who like both vanila and butterscotch.......\n";
				while (p != NULL)
				{
				
					if(p->van=='y' && p->but=='y')
					{
						cout<<p->name<<"\t"<<p->van<<"\t"<<p->but<<"\n";
						//count++;
					}
					p = p->next;				
				}
			
			}
			//cout<<"Number of elemnets in linked list:"<<count;
		}	
		void disp_EitherVanOrBut()
		{
			//int count=0;
			if (head == NULL){
				cout<<"List is empty"<<endl;
			}
			else
			{
				
				node *p = head;
				cout<<"Students who like Either vanila Or Butterscotch.......\n";
				while (p != NULL)
				{
				
					if(!((p->van=='y' && p->but=='y')||(p->van=='n' && p->but=='n')))
					{
						cout<<p->name<<"\n";
						//count++;
					}
					p = p->next;				
				}
			
			}
			//cout<<"Number of elemnets in linked list:"<<count;
		}	
		void disp_NitherVanNorBut()
		{
			//int count=0;
			if (head == NULL){
				cout<<"List is empty"<<endl;
			}
			else
			{
				
				node *p = head;
				cout<<"Students who like Either vanila Or Butterscotch.......\n";
				while (p != NULL)
				{
				
					if(p->van=='n' && p->but=='n')
					{
						cout<<p->name<<"\n";
						//count++;
					}
					p = p->next;				
				}
			
			}
			//cout<<"Number of elemnets in linked list:"<<count;
		}	
	
	
};

int main()
{
	
	printf("1 to Insert data...");
	printf("\n2 Display data.....");
	printf("\n3 Display Students who like both vanila and butterscotch......");
	printf("\n4 Display Students who like Either Vanila Or Butterscotch......");
	printf("\n4 Display Students who like Nither Vanila Nor Butterscotch......");
	printf("\n0 to Exit");
	
	int choice,p;
	char van,but;
    string nm;
	List ll;
	
		do 
		{
			cout<<"\nEnter Your Choice: ";
			cin>>choice;
			switch (choice)
			{
				case 1:
					cout<<"Enter name:  ";
					cin>>nm;
					cout<<"Do you like vanilla y/n: ";
					cin>>van;
					cout<<"Do you like butterscotch y/n: ";
					cin>>but;
					ll.insertAtEnd(nm,van,but);
					break;
				
				case 2:
					ll.display();
					break;
				
				case 3:
					ll.disp_vanAndbut();
					break;
					
				case 4:
					ll.disp_EitherVanOrBut();
					break;
				case 5:
					ll.disp_NitherVanNorBut();
					break;
			
						
			}
		} while (choice != 0);
	
}
