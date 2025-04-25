# Zadania do projektu: Aplikacja do zarządzania roślinami

## 1. **Baza danych i Backend**
### Zadania:
- [ ] **Projektowanie bazy danych**:
  - Utworzenie bazy danych (np. PostgreSQL, MySQL).
  - Tabele:
    - `users`: przechowuje dane użytkowników (id, e-mail, hasło, data rejestracji).
    - `plants`: przechowuje dane roślin (id, nazwa, opis, zdjęcie, parametr pH, wilgotność, temperatura, itp.).
    - `comments`: przechowuje komentarze użytkowników o roślinach (id, plant_id, user_id, content, created_at).
    - `wishlists`: przechowuje wishlisty roślin (id, user_id, plant_id).
    - `followers`: przechowuje powiązania między użytkownikami a obserwowanymi roślinami (user_id, plant_id).
    - `notifications`: przechowuje powiadomienia dla użytkowników o aktywności (user_id, message, read, created_at).
  
- [ ] **Tworzenie REST API**:
  - Zaplanowanie i stworzenie głównych punktów końcowych API.
  - **Zasady**: 
    - Każdy endpoint powinien mieć odpowiednie metody (GET, POST, PUT, DELETE).
    - Dodanie funkcji do walidacji danych (np. przy dodawaniu rośliny).
    - Implementacja błędów i wyjątków w API (np. 404 dla nieznalezionych zasobów).
  
### Endpoints API:
1. **Autoryzacja i Użytkownicy**:
   - `POST /auth/register` – rejestracja nowego użytkownika (z email i hasłem).
   - `POST /auth/login` – logowanie użytkownika (z email i hasłem).
   - `POST /auth/google` – logowanie za pomocą Google OAuth.
   - `POST /auth/logout` – wylogowanie użytkownika.
   - `GET /user/profile` – pobranie danych profilu użytkownika.
   - `PUT /user/profile` – edytowanie danych użytkownika (imię, zdjęcie, preferencje).

2. **Rośliny (Katalog)**:
   - `GET /plants` – pobranie listy roślin z katalogu (z filtrami: nazwa, rodzaj, itp.).
   - `GET /plants/{id}` – pobranie szczegółowych informacji o roślinie.
   - `POST /plants` – dodawanie nowej rośliny do katalogu (nazwa, opis, zdjęcie, parametry).
   - `PUT /plants/{id}` – edytowanie istniejącej rośliny.
   - `DELETE /plants/{id}` – usuwanie rośliny z katalogu.
  
3. **Komentarze**:
   - `GET /plants/{id}/comments` – pobranie komentarzy dla rośliny.
   - `POST /plants/{id}/comments` – dodawanie komentarza do rośliny.
   - `DELETE /comments/{id}` – usuwanie komentarza.
  
4. **Wishlist**:
   - `GET /user/wishlist` – pobranie wishlisty użytkownika.
   - `POST /user/wishlist` – dodawanie rośliny do wishlisty.
   - `DELETE /user/wishlist/{id}` – usuwanie rośliny z wishlisty.

5. **Znajomi i Obserwowanie**:
   - `GET /user/friends` – pobranie listy znajomych użytkownika.
   - `POST /user/friends/{id}` – dodanie znajomego (id użytkownika).
   - `DELETE /user/friends/{id}` – usunięcie znajomego.
   - `GET /plants/{id}/followers` – pobranie listy osób obserwujących daną roślinę.
   - `POST /plants/{id}/followers` – obserwowanie rośliny.
   - `DELETE /plants/{id}/followers` – przestanie obserwowania rośliny.

6. **Wykresy i Statystyki**:
   - `GET /plants/{id}/stats` – pobranie statystyk rośliny (np. wykres pH, temperatura, wilgotność).
  
7. **Powiadomienia**:
   - `GET /user/notifications` – pobranie powiadomień dla użytkownika.
   - `PUT /user/notifications/{id}/read` – oznaczenie powiadomienia jako przeczytane.
  
- [ ] **Autoryzacja i zabezpieczenia**:
  - **JWT (JSON Web Tokens)** do zabezpieczenia API.
  - **Role i uprawnienia**: administrator, użytkownik.
  - Hasła użytkowników powinny być bezpiecznie przechowywane (np. bcrypt).
  
- [ ] **Testowanie backendu**:
  - **Testy jednostkowe dla API**: Sprawdzenie poprawności zwracanych danych, kodów statusu.
  - **Testy integracyjne**: Testowanie pełnych ścieżek, np. rejestracja i logowanie użytkownika.
  - **Testy bezpieczeństwa**: Sprawdzenie ochrony przed atakami, np. XSS, SQL Injection.

---

## 2. **Katalog roślin**
### Zadania:
- [ ] **Dodawanie rośliny**:
  - Możliwość dodawania rośliny przez użytkowników (formularz z danymi: nazwa, opis, zdjęcie).
  - Weryfikacja poprawności danych (np. poprawny format zdjęcia).
  
- [ ] **Przeglądanie roślin**:
  - Strona z pełnym katalogiem roślin, gdzie użytkownicy mogą filtrować rośliny po różnych kryteriach (np. gatunek, pH, temperatura).
  - Możliwość wyszukiwania roślin po nazwie.
  - Dynamiczne ładowanie danych (np. infinite scroll).

- [ ] **Edycja i usuwanie roślin**:
  - Edytowanie danych roślin (np. opis, zdjęcie).
  - Usuwanie roślin z katalogu.
  
- [ ] **Parametry roślin**:
  - Prezentacja parametrów roślin (pH, wilgotność, temperatura, itp.) w czytelnej formie.
  - Możliwość ustawienia przypomnienia o warunkach (np. dla pH).

---

## 3. **Logowanie i Rejestracja**
### Zadania:
- [ ] **Google OAuth**:
  - Implementacja logowania za pomocą Google OAuth 2.0.
  - Integracja z frontendem (np. przycisk logowania przez Google).
  - Sprawdzanie, czy użytkownik już istnieje, jeśli nie – rejestracja.
  
- [ ] **Rejestracja i logowanie**:
  - Rejestracja użytkownika (e-mail, hasło).
  - Logowanie przez e-mail i hasło.
  - Zabezpieczenie danych użytkowników (hasła przechowywane w formie haszowanej).

---

## 4. **Wishlist roślin**
### Zadania:
- [ ] **Tworzenie wishlisty**:
  - Możliwość dodawania roślin do wishlisty.
  - Użytkownicy mogą tworzyć, edytować i usuwać swoją wishlistę.
  
- [ ] **Zakupy roślin**:
  - Umożliwienie dodania linku do sklepu, w którym można zakupić daną roślinę.

---

## 5. **Wykresy i statystyki**
### Zadania:
- [ ] **Wykresy parametrów**:
  - Generowanie wykresów dla parametrów takich jak pH, wilgotność, temperatura, EC (przewodność elektryczna).
  - Dostosowanie wykresów do historii wartości dla poszczególnych roślin.

- [ ] **Interfejs użytkownika do wykresów**:
  - Dodanie do UI opcji wyboru rośliny i daty, aby wyświetlić wykresy.

---

## 6. **Komentowanie roślin**
### Zadania:
- [ ] **Dodawanie i usuwanie komentarzy**:
  - Umożliwienie użytkownikom dodawania komentarzy pod roślinami.
  - Możliwość edytowania i usuwania komentarzy.

- [ ] **Moderacja komentarzy**:
  - Możliwość zgłaszania nieodpowiednich komentarzy.

---

## 7. **System znajomych i obserwujących**
### Zadania:
- [ ] **Obserwowanie roślin i znajomych**:
  - Umożliwienie użytkownikom dodawania znajomych i obserwowania ich roślin.
  
- [ ] **Powiadomienia**:
  - Powiadomienia dla użytkowników o nowych roślinach, które zostały dodane przez ich znajomych.

---

## 8. **Deployment i Hosting**
### Zadania:
- [ ] **Deployment na serwerze**:
  - Wdrożenie aplikacji na Heroku, AWS lub DigitalOcean.
  - Konfiguracja środowisk produkcyjnych i stagingowych.
  
- [ ] **SSL i bezpieczeństwo**:
  - Zabezpieczenie aplikacji SSL (HTTPS).
  - Weryfikacja poprawności ustawień bezpieczeństwa aplikacji.

---

## 9. **Testy i dokumentacja**
### Zadania:
- [ ] **Testy jednostkowe i integracyjne**:
  - Testowanie backendu i frontendowych funkcjonalności.
  - Sprawdzenie poprawności danych w bazie, bezpieczeństwa API.

- [ ] **Dokumentacja API**:
  - Stworzenie szczegółowej dokumentacji API z przykładami użycia.

- [ ] **Dokumentacja użytkownika**:
  - Przygotowanie materiałów dla użytkowników na temat korzystania z aplikacji.

---

## 10. **UI/UX Design**
### Zadania:
- [ ] **Prototyp UI/UX**:
  - Stworzenie prototypów UI (np. Figma, Adobe XD).
  - Usprawnienie doświadczenia użytkownika poprzez poprawę intuicyjności interfejsu.

---

To jest szczegółowy plan zawierający API i bardziej granularne zadania. Jeśli chcesz wprowadzić jakiekolwiek zmiany lub dostosowania, daj mi znać!
