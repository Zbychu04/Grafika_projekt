LIBS=-lGL -lglut -lGLU

main_file: main_file.cpp
	g++ -o main_file main_file.cpp $(LIBS)
