#include<iostream> 
using namespace std;

int main()
{
    // an array with 4 rows and 4 columns.
    int a[4][4] = {
        { 2, 4, 1, 3 },
        { 1, 3, 2, 4 },
        { 3, 2, 4, 1 },
        { 4, 1, 3, 2 }
    };

    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++) {

            cout << "a[" << i << "][" << j << "]: ";
            cout << a[i][j] << endl;
        }

    return 0;
}
