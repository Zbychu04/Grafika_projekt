#ifndef OBJPARSER_H
#define OBJPARSER_H

#include <iostream>
#include <cstdlib>
#include <vector>

class ObjParser {
    public:
        static void objToTxt(const std::string aInFilename,
                const std::string aOutFilename,
                bool aVerbose = false);
        static std::vector<std::string> explode(std::string aStr, char aDelim);
};
#endif
