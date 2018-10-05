# A scaffold for Valkka python modules

## Synopsis

This is a scaffold for creating python-only extensions for Valkka.  For more details, see [here](https://elsampsa.github.io/valkka-examples/_build/html/modules.html)

The python module is created under the valkka.* namespace.

## Creating a package

Let's create a package *valkka_gimmick* that is using namespace *valkka.gimmick*.  Proceed like this:

    git clone git@github.com:elsampsa/valkka-skeleton.git
    cp -r valkka-skeleton gimmick
    cd gimmick
    ./reinit.bash
    
After this, the directory has been renamed from "gimmick" to "valkka_gimmick" and the module has been installed in development mode.  Check that it works with:

    ipython3
    from valkka import gimmick
    
.. and explore the "gimmick" namespace

<!--- Once you have created your own python package and uploaded it into git(hub), uncomment this section 

## Installing

### Development

Install with:

    git clone git://github.com/[name of your git repo]/valkka-skeleton.git
    cd valkka-skeleton
    pip3 install --user -e .

After that, you can access the documentation with:
    
    firefox docs/index.html
    
### Production

Install with:

    pip3 install git+git://[name of your git repo]/valkka-skeleton


-->

## Authors
Sampsa Riikonen

## Copyright
(C) 2018 Sampsa Riikonen

## License
MIT


