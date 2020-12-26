#include <iostream>
using namespace std;

int main()
{
    //initialise rows and columns
    int rows = 4; 
    int columns = 4;

    // an array with 4 rows and 4 columns.
    int a[4][4] = {
        { 2, 4, 1, 3 },
        { 1, 3, 2, 4 },
        { 3, 2, 4, 1 },
        { 4, 1, 3, 2 }
    };

    //display array in a matrix format
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            cout << a[i][j] << "\t";
        }
        cout << endl;
    }
    return 0;
}
