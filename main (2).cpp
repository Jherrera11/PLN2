#include <iostream>
#include <string.h>
using namespace std;

//DECLARACION DE LA CLASE

class Empleado
{
    //ATRIBUTOS
    private: //Nivel de acceso
    char Nombre[50]
    float V;
    float Sueldo;
    float Comision;
    //METODOS
    public: //Nivel de acceso
    void Ingresar_Datos();
    void Imprimir_Datos();
    Empleado(); //Constructor Normal
    Empleado(char*n,float V,float Sueldo,float Comision); //Constructor por parametros
    ~Empleado(); //Destructor
    float Calcular_Salarios();
    float Calcular_Comision();
    float V();
};

int main()
{
    //INSTANCIA DE LA CLASE EMPLEADOS
    Empleado uno; //Creacion de los datos del primer empleado

    cout<<"Empleado uno: "<<endl<<endl;
    uno.Ingresar_Datos();
    uno.Imprimir_Datos();


    return 0;
}


void Empleado::Ingresar_Datos()
{
    cout<<"Ingresar el Nombre del empleado"

}
