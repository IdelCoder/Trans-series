#! /bin/bash

touch fb15k.log
f=fb15k.log

cd TransE
echo "running transE `date`" >> ../$f && python transE.py
echo "running transE-ag `date`" >> ../$f && python transE-ag.py
echo "running transE-pos `date`" >> ../$f && python transE-pos.py

cd ../TransH
echo "running transH `date`" >> ../$f && python transH.py
echo "running transH-ag `date`" >> ../$f && python transH-ag.py
echo "running transH-pos `date`" >> ../$f && python transH-pos.py

cd ../TransR
echo "running transR `date`" >> ../$f && python transR.py
echo "running transR-ag `date`" >> ../$f && python transR-ag.py
echo "running transR-pos `date`" >> ../$f && python transR-pos.py

cd ../TransD
echo "running transD `date`" >> ../$f && python transD.py
echo "running transD-ag `date`" >> ../$f && python transD-ag.py
echo "running transD-pos `date`" >> ../$f && python transD-pos.py

cd ../TransM
echo "running transM `date`" >> ../$f && python transM.py
echo "running transM-ag `date`" >> ../$f && python transM-ag.py
echo "running transM-pos `date`" >> ../$f && python transM-pos.py

cd ../STransE
echo "running stransE `date`" >> ../$f && python STransE.py
echo "running STransE-ag `date`" >> ../$f && python STransE-ag.py
echo "running STransE-pos `date`" >> ../$f && python STransE-pos.py

