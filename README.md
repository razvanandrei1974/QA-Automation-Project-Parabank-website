# QA-Automation-Project-Parabank-website 🔄( Under Construction)

📍 Am creat planul de testare automată cu Behave pentru meniul de _"Login"_ și meniul _"Register"_ pentru aplicația Parabank. 
📍 Am folosit Selenium pentru a automatiza acțiunile de navigare și interacțiune cu interfața web. 

## 📌 Instalare și configurare:

🖥️ Am instalat Behave, Selenium, WebDriver pentru Python.

▶️ Definirea scenariilor de testare:

Se deschide un fișier _.feature_ pentru a defini scenariile de testare, atat pentru meniul **Login** cat și pentru **Register**.
Am definit scenariile de testare pentru diferite cazuri de utilizare, cum ar fi:

▶️ Login cu succes utilizând credențiale valide.
![image](https://github.com/razvanandrei1974/QA-Automation-Project-Parabank-website/assets/144438182/088896cf-7d47-4acd-86ed-3c8491e43b7a)

▶️ Login eșuat cu credențiale invalide.



Validarea mesajelor de eroare pentru câmpurile obligatorii la login și înregistrare.
Înregistrare cu succes cu date valide.
Înregistrare eșuată cu date invalide.
📩 Implementarea pasilor de testare:

Pentru fiecare scenariu definit în fișierul .feature, implementează pașii de testare în fișierul steps.py.
```
from selenium.webdriver.common.by import By

from browser import Browser

class LoginPage(Browser):

    USERNAME_FIELD_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/form/div[1]/input')
    PASSWORD_FIELD_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/form/div[2]/input')
    LOGIN_BUTTON_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/form/div[3]/input')
    MESSAGE_ERROR_LABEL = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/p')

    def navigate_to_login_page(self):
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")

    def enter_username(self, jhon1234):
        self.driver.find_element(*self.USERNAME_FIELD_SELECTOR).send_keys(jhon1234)

    def enter_password(self, demo):
        self.driver.find_element(*self.PASSWORD_FIELD_SELECTOR).send_keys(demo)


    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON_SELECTOR).click()

    def get_error_message(self):
        return self.driver.find_element(*self.MESSAGE_ERROR_LABEL).text
```

Folosește Selenium pentru a automatiza acțiunile de navigare și interacțiune cu elementele din interfața web.
Exemplu de pași de testare pentru login ar putea fi:
Navigare către pagina de login.
Introducerea numelui de utilizator și a parolei.
Apăsarea butonului de login.
Validarea succesului sau eșecului login-ului în funcție de rezultatul așteptat.
Configurare pentru rularea testelor:

Asigură-te că fiecare scenariu are o stare inițială bine definită, de exemplu, fiecare test ar trebui să înceapă de pe pagina de start a aplicației.
Configurarea Selenium WebDriver pentru a interacționa cu browser-ul dorit (de exemplu, Chrome, Firefox etc.).
Poți folosi parametri de configurare pentru a seta URL-ul aplicației Parabank, numele de utilizator și parola într-un mod flexibil.
Rularea testelor:

Folosește Behave pentru a rula testele definite.
Asigură-te că rularea testelor afișează rezultatele testelor și orice mesaje de eroare sau avertismente.
Raportare și remediere:

Interpretează rezultatele testelor și identifică orice erori sau probleme.
Remediază problemele întâlnite și retestează pentru a te asigura că aplicația funcționează corect conform specificațiilor.
Acest plan de testare automată cu Behave ar trebui să îți ofere un început pentru a automatiza testarea meniului de login și de înregistrare pentru aplicația Parabank
