#include <stdio.h>

void printArray(int arry[],int len){
	int i;
	for(i=0;i<len;i++){
		printf("%d ",arry[i]);
	}
	printf("\n");
}

void insertionSort(int arry[],int len){
	int i,j;
	for(i=1;i<len;i++){
		int insertNumber=arry[i];
		for(j=i-1;j>=0;j--){
			if(arry[j]<insertNumber)
			break;
			arry[j+1]=arry[j];
		}
		arry[j+1]=insertNumber;
	}
}

int main(){
	int nums[]={4,3,1,3,2};
	printArray(nums,5);
	insertionSort(nums,5);
	printArray(nums,5);
}
