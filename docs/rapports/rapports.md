Contenu d’un rapport minimal pour le Module 0


Objectif : trois microservices Flask, règle de TVA en entiers, tests pytest.
Environnement : Windows, Git Bash, Python 3.12.0, versions de Flask/pytest (pip list).

Résultats des tests : 4 passed, et le tableau des curl avec les réponses obtenues.
MARC DIDIER@DESKTOP-I6E3ANP MINGW64 ~/facturecloud
$ python -m pytest -v
============================= test session starts =============================
platform win32 -- Python 3.12.0, pytest-9.1.1, pluggy-1.7.0 -- C:\Users\MARC DIDIER\facturecloud\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\MARC DIDIER\facturecloud
configfile: pytest.ini
collecting ... collected 4 items

tests/unit/test_tva.py::test_tva_arrondie_au_franc_le_plus_proche PASSED [ 25%]
tests/unit/test_tva.py::test_tva_sur_20000 PASSED                        [ 50%]
tests/unit/test_tva.py::test_tva_sur_zero PASSED                         [ 75%]
tests/unit/test_tva.py::test_tva_negative_leve_erreur PASSED             [100%]

============================== 4 passed in 0.09s ==============================
(.venv)

MARC DIDIER@DESKTOP-I6E3ANP MINGW64 ~
$ curl http://localhost:8090/sante
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    16  100    16    0     0     75      0 --:--:-- --:--:-- --:--:--    75{"statut":"ok"}


MARC DIDIER@DESKTOP-I6E3ANP MINGW64 ~
$ curl http://localhost:8081/sante
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    16  100    16    0     0     72      0 --:--:-- --:--:-- --:--:--    73{"statut":"ok"}


MARC DIDIER@DESKTOP-I6E3ANP MINGW64 ~
$ curl http://localhost:8082/sante
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    16  100    16    0     0     78      0 --:--:-- --:--:-- --:--:--    78{"statut":"ok"}

MARC DIDIER@DESKTOP-I6E3ANP MINGW64 ~
$ curl "http://localhost:8081/tva?montant=20000"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    32  100    32    0     0    154      0 --:--:-- --:--:-- --:--:--   154{"montant_ht":20000,"tva":3850}


MARC DIDIER@DESKTOP-I6E3ANP MINGW64 ~
$ curl http://localhost:8090/factures/FC-0000-000001
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    30  100    30    0     0    146      0 --:--:-- --:--:-- --:--:--   147{"erreur":"FACTURE_INCONNUE"}

Service  	                Port	Réponse
api-factures	                8090	{"statut":"ok"}
service-calcul	                8081	{"statut":"ok"}
service-notifications	        8082	{"statut":"ok"}

Problèmes rencontrés et solutions : 
python3 inexistant, donc python.
Activation du venv par Scripts et non bin.
Port 8080 occupé (WinError 10013), service lancé sur 8090.