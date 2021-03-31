# Скрипты для расчетов на Ломоносове-2

1. Сборка программ на C++:
```
mpicxx prog.cpp -o prog.exe
mpicxx prog_bug.cpp -o prog_bug.exe
```

2. Положите папку с гауссианом по адресу `l2_scripts/g16sse`

3. Скопируйте всю директорию на сетевой диск и перейдите туда:
```
cp -R . ~/_scratch/my_calculations
cd ~/_scratch/my_calculations
```

4. Создать папку с инпут-файлами и куда надо сохранять логи:
```
mkdir inputfiles; cd inputfiles
scp *gjf lomonosov2:~/_scratch/my_calculations/inputfiles/ # На своем компьютере
```

5. Создать файл со списком расчетов `do_calc.dat`:
```
for i in *gjf
do
echo inputfiles/$i >> do_calc.dat
done
mv do_calc.dat ~/_scratch/my_calculations/inputfiles/
```

6. Поправить файл `calc.sh`. Впишите правильное число нодов в строку `#SBATCH --cpus-per-task=1` и, если не хотите, чтобы каждый нод делал больше одного расчета, то поменяйте в последней строке `./prog_bug.exe` на `./prog.exe`.
