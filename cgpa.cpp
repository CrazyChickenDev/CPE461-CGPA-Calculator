/*
A little test run project on the gpacalculator using c in order to implement for the cgpa actual assignment
*/


#include <iostream>
#include<cstring>
using namespace std;
class gpa {						// Class for calculating gpa 
private:
	double creditH[25];				// Store the credit hours of student	
	string grade;					
	string gradeList[20];				// To get the list of grades
	double gpa;
	double credit = 0;
	double sum = 0;
public:
	int number_of_subjects;
	void enterGrade();
	void evaluate();				// Compute the grades of student
	float TotalGpa();				// Computes the gpa of enter grades
};
void gpa::enterGrade()
{
	for (int i = 0; i < number_of_subjects; i++)			// Run for number of subjects time
	{
		cout << "Please enter the grade of " << i + 1 << " subject:";
		cin >> gradeList[i];								// input the enter grade in gradeList
		cout << "Please enter the credit hour of " << i + 1 << " subject:";
		cin >> creditH[i];								// input the entered credit hours in creditH
		credit = credit + creditH[i];							// add the creditH in credit
	}
	
}
void gpa::evaluate()
{	for (int i = 0; i < number_of_subjects; i++)
	{
		grade = gradeList[i];
		if (grade[0] == 'A' && grade[1]=='\0')				// Compute if grade entered is 'A' in capital format
		{
			gpa = (4 * creditH[i]);					// calculate the gpa 
			sum = sum + gpa;
		}
		else if (grade[0] =='A' && grade[1]=='+')			// Compute if grade entered is 'A+' in capital format
		{
			gpa = (4 * creditH[i]);
			sum = sum + gpa;
		}
		else if (grade[0] == 'A' && grade[1]=='-')  {			// Compute if grade entered is 'A-' in capital format
			gpa = 3.7 * creditH[i];
			sum = sum + gpa;
		}
		else if (grade[0] == 'B' && grade[1] == '+') {			// Compute if grade entered is 'B+' in capital format
			gpa = 3.3 * creditH[i];
			sum = sum + gpa;
		}
		else if (grade[0] == 'B' && grade[1]=='\0') {			// Compute if grade entered is 'B' in capital format
			gpa = 3.0 * creditH[i];
			sum = sum + gpa;
		}
		else if (grade[0] == 'B' && grade[1] == '-') {			// Compute if grade entered is 'B-' in capital format
			gpa = 2.7 * creditH[i];
			sum = sum + gpa;
		}
		else if (grade[0] == 'C' && grade[1] == '+') {			// Compute if grade entered is 'C+' in capital format
			gpa = 2.3 * creditH[i];
			sum = sum + gpa;
		}
		else if (grade[0] == 'C' && grade[1] == '\0') {			// Compute if grade entered is 'C' in capital format
			gpa = 2.0 * creditH[i];
			sum = sum + gpa;
		}
		else if (grade[0] == 'C' && grade[1] == '-') {			// Compute if grade entered is 'C-' in capital format
			
			gpa = 1.7 * creditH[i];
			sum = sum + gpa;
		}
			else if (grade[0] == 'D' && grade[1]=='+') {		// Compute if grade entered is 'D+' in capital format
			gpa = 1.3 * creditH[i];
			sum = sum + gpa;
		}
		else if (grade[0] == 'D' && grade[1] == '\0'){			// Compute if grade entered is 'D' in capital format
			gpa = 1.0 * creditH[i];
			sum = sum + gpa;
		}
		else if (grade[0] == 'F') {					// Compute if grade entered is 'F' in capital format
			gpa = 0.0 * creditH[i];	
			sum = sum + gpa;
		}
	}
}
float gpa::TotalGpa()
{
	float total=(float)sum / credit;			// Calculate the total gpa
	return total;
}
int main()
{
       gpa cg
	cout << "Please enter the number of subjects of the current semester in which you are studying: ";
	cin >> g.number_of_subjects;
	g.enterGrade();
	g.evaluate();
	double totalGpa = g.TotalGpa();
	cout << "Your total gpa is " << totalGpa;
	return 0;
}
