#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <numeric>
using namespace std;
bool decreciente (int i,int j) { return (i>j); }
bool algo(vector <int> *vec){
    int inicial=(*vec)[0];

    int dif=0;
    int nuevoMedio =((*vec)[0]/2) + ((*vec)[0] %2);

    while (((*vec)[dif] > nuevoMedio)&&(dif < (*vec).size())){
        dif++;
    }
    return ((nuevoMedio+dif)<inicial);
}
void  comer( vector <int> *vec){
    std::vector<int>::iterator rmv;
    bool ers=false;
    for (std::vector<int>::iterator it=(*vec).begin(); it!=(*vec).end(); ++it){
        (*it)--;
        if ((*it)==0){
            rmv=it;
            ers=true;
            break;
        }
    }
    if (ers){
        (*vec).erase(rmv,(*vec).end());
    }


}
/**
* a contiene un valor
*
*/
int agregar(vector <int> *vec){
int a,nuevoMedio =((*vec)[0]/2) + ((*vec)[0] %2),cont=0;
for (int i=0;(*vec)[i]>nuevoMedio;i++){
    a=((*vec)[i])/2 + ((*vec)[i])%2;
    (*vec)[i]/=2;
    (*vec).push_back(a);
    cont++;
}

 return cont;


}
int main()
{
    int contador,aux,cantidad,panq,minutos;
    vector <int> vec;

    cin >> contador;
    aux=contador;
    while (contador--)
    {   minutos=0;
        cin >> cantidad;
        for (int i=0; i<cantidad; i++)
        {
            cin >> panq;
            vec.push_back(panq);
        }
        sort(vec.begin(),vec.end(),decreciente);
        while (!vec.empty())
            { //pasa el tiempo

            if (algo(&vec))
                {

                    minutos+=agregar(&vec);
                    sort(vec.begin(),vec.end(),decreciente);
                }
            else
                {
                minutos++;
                comer(&vec);
            }


        }
        cout <<"Case #"<<aux-contador<<": "<< minutos<<endl;
    }



    return 0;
}