#include <iostream>
#include <dirent.h>
#include <fstream>
#include <string>


using namespace std;
int main()
{   
    string tmp, result;
    ifstream myread("book.txt");
    while (getline(myread, tmp)){
        cout << tmp;
    }
    myread.close();

} // namespace std;

