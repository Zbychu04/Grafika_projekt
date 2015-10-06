#include <GL/gl.h>
#include <GL/glut.h>
#include <stdio.h> //Przydatne do wypisywania komunikatów na konsoli
#include "glm/glm.hpp"
#include "glm/gtc/matrix_transform.hpp"
#include "glm/gtc/type_ptr.hpp"

void displayFrame(void) {

}


int main(int argc, char* argv[]) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(800, 800);
	glutInitWindowPosition(0, 0);
	glutCreateWindow("Program OpenGL");
	glutDisplayFunc(displayFrame);

	//Tutaj kod inicjuj¹cy

	glutMainLoop();
	return 0;
}
