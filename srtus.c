16.1.1.
You are assigned a project to design a Student Data Entry and Management System for
your college. The system should simulate how data flows and is accessed in a real
academic structure — from the Principal to the Class Teacher to the Class
Representative (CR).
Each class has a Class Representative (CR) who holds specific information such as:
Name
Roll Number
Contact Number
Email
The Principal should be able to access and update the CR’s information, but the access
should follow the hierarchy:
Principal ? Class Teacher ? CR
You are required to:
Define a struct CR to store the details of the Class Representative.
Use a pointer to pointer to struct CR to simulate this control flow — showing how the
Principal accesses the CR’s data through the Class Teacher.
Write functions to:
Initialize the CR details.
Display CR details.
Update CR details via the Principal (using pointer to pointer).
Demonstrate the data flow in your main() function, clearly showing how the Principal
communicates through the Class Teacher to update or view the CR’s information.
Expected Features:
Use of struct to define CR data.
Use of struct CR* by Class Teacher.
Use of **struct CR** (pointer to pointer) by Principal to access CR data.
Functionality for the Principal to update CR’s contact number or email via pointer to
pointer.
Clearly commented code showing role simulation (Principal, Class Teacher, CR).
Testcase:
--- Initial CR Details ---
Name: Rahul Sharma
Roll No: 101
Contact: 9876543210
Email: rahul.sharma@email.com
Principal wants to update contact and email...
--- Updated CR Details ---
Name: Rahul Sharma
Roll No: 101
Contact: 9123456789
Email: cr.rahul@college.edu
#include <stdio.h>
#include <string.h>

typedef struct {
    char name[50];
    int rollNo;
    char contact[15];
    char email[50];
} CR;

void initializeCR(CR *cr, char *name, int rollNo, char *contact, char *email) {
    strcpy(cr->name, name);
    cr->rollNo = rollNo;
    strcpy(cr->contact, contact);
    strcpy(cr->email, email);
}

void displayCR(CR *cr) {
    printf("Name: %s\nRoll No: %d\nContact: %s\nEmail: %s\n", cr->name, cr->rollNo, cr->contact, cr->email);
}

void updateCR(CR **cr, char *newContact, char *newEmail) {
    strcpy((*cr)->contact, newContact);
    strcpy((*cr)->email, newEmail);
}

int main() {
    CR cr;
    initializeCR(&cr, "Rahul Sharma", 101, "9876543210", "rahul.sharma@email.com");

    printf("--- Initial CR Details ---\n");
    displayCR(&cr);

    CR *classTeacher = &cr;
    CR **principal = &classTeacher;

    printf("\nPrincipal updating contact and email...\n");
    updateCR(principal, "9123456789", "cr.rahul@college.edu");

    printf("\n--- Updated CR Details ---\n");
    displayCR(&cr);
    return 0;
}
