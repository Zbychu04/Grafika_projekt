#ifndef OBJPARSER_H
#define OBJPARSER_H

using namespace std;

class ObjParser {
    public:
        static void objToTxt(const string aInFilename,
                const string aOutFilename,
                bool aVerbose = false);
        static vector explode(string aStr, char aDelim);
};
#endif
