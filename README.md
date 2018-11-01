# RTR105
### datormacības elektroniskā klade
### 2.nodarbības komandas
1. **whoami** - uzzināt kas es esmu.
2. **who** - uzzināt kas ir blakus mani.
3. **pwd** - uzzināt manu atrašanas vietu sistēmā.
4. **ls**- parāda direktorijas saturu.
5. **ls -l** - parāda papildus info.
6. **ls -a** - parāda slēptus failus (sākas ar punktu) direktorijā.
7. **ctrl+alt+T** - atvērt terminālu.
8. **ctrl+l** - nodzest visu lieko.
9. **"burts" + 2x TAB** - uzzināt visus iespejamus komandus ar šo burtu.
10. **crtl+alt+f1** - pārslēgties uz teksta (komandrindas) saskarni.
11. **ctrl+alt+f7** - atgriezties atpakaļ grafiskajā saskarnē.
12. **uname -a** - uzzināt Linux versiju.
13. **firefox &** - atvērt Internet tīklu.

     :joy::ok_hand:
     
### 3.nodarbības komandas
1. **cd "direktorijas nosaukums"** - pārvietoties uz citu direktoriju.
2. **.** - pašreizējā darba mape.
3. **..** - pašreizējas darba mapes vecākmape.
4. **/** - failsistēmas sakne.
5. **~** - pašreizējā lietotāja mājas mape.
6. **echo** - attēlo komandrindā uzrakstītu tekstu
7. **echo "TEXT" >> file.txd** - pārveidot tekstu faila.
7. **mkdir** - izveido jaunas mapes.
8. **rmdir** - nodzēst mapes.
9. **rm** - džes failus un mapes.
10. **mv** - pārvieto datnes un mapes.
11. **man** - sniedz informāciju par citām komandām.

### 4.nodarbības komandas
1. **mans_skripts.sh** - izpildīt uzdoto skriptu.
2. **echo $PATH** - sistēmas mainīga, ar kuru var manīt ceļu līdz failam.
3. **./mans_skripts.sh** - ieiet skriptā.
4. **/home/user/mans_skripts.sh** - ieiet skriptā.
5. **~/mans_skripts.sh** - ieiet skriptā.
5. **cat mans_skripts.sh** - lasīt skripta satūru.
6. **cat/bin/ls** - izlasīt direktorijas satūru.
7. **chmod 764 mans_skripts.sh** - izmainīt tiesības skriptam, lai tas varētu strādāt.

### 5.nodarbības svarīga informācija
1. **idle &** - parslēgties uz "idle" vidi.
2. **python** - parslēgties uz "python" vidi.
3. **ipython** - parslēgties uz "ipython" vidi.
4. **"TAB"** - var noskatities iespējamas komandas.
5. **git clone https://github.com/next51/RTR105** - ieiet sava repositarijā.

### 7.nodarbība: Variables, expressions and statements.
1. **_print()_** - attēlot tekstu komandrindā.
2. **_x = .. ; y = .., z = .._** - uzdot mainīgus.
3. **_type()_** - uzzināt kādai funkcijai pieder simbols.
4. mes varam izmantot **_int()_** and **_float()_** lai invertēt **int** to **str** / **str** to **int** 
5. mes varam izmantot **_input()_**, lai uzdot lietotajam jautajumu.Piemeram:
~~~
 name=input('Who are you?')
 print('Welcome',name)
~~~
### 8. nodarbība: Conditional Execution.
1. **_if_** - uzdot nosacījumu.
2. **If you mix _tabs_ and _spaces_, you may get _“indentation errors”_ even if everything looks fine**
3. **_if_** .. **_else_** - mes varam vienlaicīgi uzdot divus nosacījumus.
   ~~~
   x = 4
   if x > 2:
      print('Bigger than two')
   else:
      print('Smaller than two')
   ~~~
4. **_if_** ; **_elif_** ; **_else_** - izmantojam tādu konstrukciju,lai uzdot 3 vai vairākus nosācijumus.
5. **==** - vienāds ar ;   **!=** - nav vienāds ar ;   **<=** - mazāks vai vienāds ar ;   **=>** - lielāks vai vienāds ar 

### 9. nodarbība: Loops and Iterations.
1. Pythona ir divu veidu funkcijas - **_built-in funkcijas_** (piem., print(), input(), type(), float(), int() ) un funkcijas, kuru definējam **_mēs_** un pēc tam izmantojam.
2. Lai apzīmet savu funkciju izmanto **'def'**
3. Mēs varam uzdot savai funkcijai parametrus. Piemēram:
~~~
>>> def greet(lang):
... if lang == 'es':
... print('Hola')
... elif lang == 'fr':
... print('Bonjour')
... else:
... print('Hello')
...
>>> greet('en')
Hello
>>> greet('es')
Hola
>>> greet('fr')
Bonjour 
~~~
4. **_return_** - izmanto, lai dabūt fankcijas rezultātu.
5. Funkcijai var uzdot vairākus argumentus. Piemerām:
~~~
def addtwo(a, b):
 added = a + b
 return added
x = addtwo(3, 5)
print(x)
8
~~~

### 10. nadarbība: Loops and Iteration
1. 
2. 
3. 
4. 
5. 

### 11. nodarbība: Strings.
1. **_str = '..'_** - izmanto, lai uzrakstīt virkni
2. Mēs var uzzināt jebkuru simbolu rindā, izmantojot **_[]_** Piemierām:
~~~
fruit = 'banana'
>>> letter = fruit[1]
>>> print(letter)
a
>>> x = 3
>>> w = fruit[x - 1]
>>> print(w)
n
~~~
3. **_Jāatcerās, ka simbolu rinda sākas no 0_** (0 1 2 3 4 5 6...)
4. **_lem_** - uzzināt cik simboli ir vienā rindā:
~~~
>>> fruit = 'banana'
>>> print(len(fruit))
6
~~~
5. **_[0:4]_** - apskatīt, kas atrodas starp 0 un 4 (neieskaitot) elementiem.
6. **_'n' in string_** - uzzināt vai rindā ir burts 'n'.
7. **_.lower_** - uzrakstīt visu rindu ar maziem burtiem.
8. **_.upper_** - uzrakstīt visu rindu ar lieliem burtiem.
9. **_.find('n')_** - uzzināt kāda pozīcija atrodas burts 'n'. Jā tada nav, tad rezultāts būs -1.
10. **_.replace('Bob''Jane')_** - izmainīt rindā vārdu 'Bob' uz 'Jane'.
11. **_.lstrip/rstrip/strip_** - nodzēst atstarpes kreisajā / labajā / abas pusēs.
12. **_startswith('n')/endswith('n')_** - pāŗbaudit vai rinda sākas / beidzas ar burtu 'n'.
