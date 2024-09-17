## Get the code

Option1:

Go to the "exploring_laplacian_graphics_course" folder, where you can Download the zip

Option2:

Type the following in your terminal (this is using git):

    git clone https://github.com/HeCraneChen/exploring_laplacian_graphics_course.git --recursive



## MacOS 

You will access CMake from terminal. First, install HomeBrew, then in the terminal run:

    brew install cmake

**Compile**

    cd week3
    cd HelloGraphics
    mkdir build
    cd build
    cmake ..
    make

**Run**

    ./HelloGraphics

## Windows (Visual Studio)

You will access CMake through Visual Studio.

**Compile**

Open the Visual Studio IDE, and click the following

`Open a local folder` and open the week3 folder cloned from this repo

`File`  `Open`  `CMake...` and open the CMakeLists.txt

`Build`  `Build All`


**Run**

    cd week3
    
    mkdir build
    
    scp ./out/build/x64-Debug/HelloGraphics.exe ./build/HelloGraphics.exe
    
    scp ./out/build/x64-Debug/_deps/gmp-src/lib/libgmp-10.dll ./build/libgmp-10.dll
    
    cd build
    
    HelloGraphics
    



