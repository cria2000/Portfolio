#include<iostream>
#include<string>
using namespace std;
template<class T>
class MyContainer{
	public:
		MyContainer(){
			obj_arr=nullptr;
			n_elements=0;
		}
		MyContainer(int n){
			obj_arr=new T[n];
			n_elements=n;
		}
//		MyContainer(T* arr, int n){
//			for(int i=0;i<n;i++)
//				obj_arr[i]=arr[i];
//			n_elements=n;
//		}
		~MyContainer(){
			n_elements=0;
			if(obj_arr!=NULL) delete obj_arr;
		}

		void clear(){
			n_elements=0;
		}
		int size() const{
			return n_elements;
		}

	protected:
		T* obj_arr;
		int n_elements;
};
template<class T>
class MyVector : public MyContainer<T>{
	public:
		MyVector(){
			capacity=0;
		}
		MyVector(int n):MyContainer<T>(){
			MyContainer<T>::obj_arr=new T[n];
			capacity=n;
		}

		MyVector<T>&operator=(const MyVector<T>& rhs){
			MyContainer<T>::n_elements=rhs.n_elements;
			capacity=rhs.capacity;
			for(int i=0;i<MyContainer<T>::n_elements;i++)
				MyContainer<T>::obj_arr[i]=rhs.obj_arr[i];
		}

		bool empty()const{
			if(capacity==0) return true;
			else return false;
		}
		int max_size()const{
			return capacity;
		}

		void reserve(int new_cap){
			T* arr=new T[new_cap];
			for(int i=0;i<MyContainer<T>::size();i++)
				arr[i]=MyContainer<T>::obj_arr[i];
		//	delete MyContainer<T>::obj_arr;
			MyContainer<T>::obj_arr=new T[new_cap];
			for(int i=0;i<MyContainer<T>::size();i++)
				MyContainer<T>::obj_arr[i]=arr[i];
		//	delete arr;
			capacity=new_cap;
			
		
		}
		void push_back(T obj){
			if(MyContainer<T>::n_elements==capacity) reserve(max(1,2*max_size()));
//			T* arr=new T[MyContainer<T>::n_elements];
//			for(int i=0;i<MyContainer<T>::n_elements;i++)
//				arr[i]=MyContainer<T>::obj_arr[i];
//			MyContainer<T>::obj_arr=new T[MyContainer<T>::n_elements];
			MyContainer<T>::obj_arr[MyContainer<T>::n_elements]=obj;
//			for(int j=0;j<MyContainer<T>::n_elements;j++)
//				MyContainer<T>::obj_arr[j]=arr[j];
			MyContainer<T>::n_elements+=1;
			
		
		}
		void pop_back(){
			MyContainer<T>::n_elements-=1;
		}
		T& at(const int idx){
			return MyContainer<T>::obj_arr[idx];
		}
		T& front(){
			return MyContainer<T>::obj_arr[0];
		}
		T& back(){
			return MyContainer<T>::obj_arr[MyContainer<T>::n_elements-1];
		}
		const T& at(const int idx) const{
			return MyContainer<T>::obj_arr[idx];
		}
		T& operator[](const int idx){
			return MyContainer<T>::obj_arr[idx];
		}
		const T& operator[](const int idx) const{
			return MyContainer<T>::obj_arr[idx];
		}

		MyVector<T>operator+(const MyVector<T>&rhs){
			MyVector<T> new_vec(capacity+rhs.max_size());
			new_vec.n_elements=MyContainer<T>::size()+rhs.size();
			for(int i=0;i<MyContainer<T>::size();i++)
				new_vec.obj_arr[i]=MyContainer<T>::obj_arr[i];
			for(int j=0;j<rhs.size();j++)
				new_vec.obj_arr[MyContainer<T>::size()+j]=rhs.obj_arr[j];
		
		
//			T* arr=new T[capacity+rhs.max_size()];
//			for(int i=0;i<MyContainer<T>::size();i++)
//				arr[i]=MyContainer<T>::obj_arr[i];
//			for(int j=0;j<rhs.size();j++)
//				arr[MyContainer<T>::size()+j]=rhs.obj_arr[j];
//			MyVector<T> new_vec;
//			cout<<MyContainer<T>::size()<<endl;
//			cout<<rhs.size()<<endl;
//			new_vec.n_elements=MyContainer<T>::n_elements+rhs.n_elements;
//			new_vec.capacity=capacity+rhs.capacity;
//			for(int i=0;i<new_vec.n_elements;i++)
//				new_vec.obj_arr[i]=arr[i];


			return new_vec;
		}
	private:
		int capacity;
};










