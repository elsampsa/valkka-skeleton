#!/bin/bash
name=$(basename $PWD)
if [ "$name" == "valkka_skeleton" ] || [ "$name" == "valkka-skeleton" ]
then
  echo will not overwrite default skeleton directory!
  exit
fi
echo initializing project $name

pwd=$PWD
cd valkka
mv skeleton $name
cd $pwd

# replace project names

fs="test_upload.bash upload.bash README.md MANIFEST.in setup.py docs/* valkka/*/*.py valkka/*/*/*.py valkka/*/*/*/*.py valkka/README.md"
for f in $fs
do
  find $f -exec sed -i "s/skeleton/$name/g" {} \;
  find $f -exec sed -i "s/Skeleton/$name/g" {} \;
  find $f -exec sed -i "s/your_package_name/$name/g" {} \;
done
# decouple from git
rm -rf .git .gitignore

cd ..
mv $name valkka_$name
cd valkka_$name

pip3 install --user -e .

# TODO: install in development mode
# recompile documentation
# cd docs
# ./compile.bash # we can compile documentation only after this module is on the pythonpath!
# cd ..
# decouple from git
rm -rf .git .gitignore

