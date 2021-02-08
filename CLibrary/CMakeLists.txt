cmake_minimum_required(VERSION 3.17)
project(CurveMatchingPython)

set(CMAKE_CXX_STANDARD 20)

add_executable(CurveMatchingPython
        main.cpp
        Indexes.h
        Spline.h
        GlobalVariables.h
        BasisFunction.h Results.h CurveMatchingPython.h)