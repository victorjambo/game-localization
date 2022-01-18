# Alocai Fullstack Software Engineer code challenge

## Scenario

In Alocai we focus on building tools for making game localization easy. This includes projects management, orders management, jobs coordination, people & companies management, accounting, machine translation, among others. Basically, we provide to linguist service providers (LSP) and game studios (GS) a complete ecosystem to be able to run a game localization process from start to end.

In this code challenge, you're asked to build a very basic version of our games management tool, so LSP's and GS's can work together creating, reading, updating and deleting video game translations projects.

## General requirements

1. Create a fully dockerized frontend and backend apps based on the descriptions provided below.
2. The code should be stored in the common GitHub repository and contain README describing how to run tests and local deployment.
3. Handle possible errors and edge cases.

## Backend

### Requirements ✅

1. Create a Python (>= 3.8) web application using web framework you find appropriate (we
   use Flask) and implement endpoints presented below
2. The application is covered by unit and integration tests using pytest
3. Application uses PostgreSQL as database

### Endpoints to implement ✍️

1. `POST /api/v1/games`

   - Validates the payload and saves the game into DB
   - If a game with already existing name was soft-deleted that name can be used again
   - Request payload schema:

   ```json
   {
     "name": "Diablo 112", // unique, not empty string
     "available_languages": ["en", "de", "ru", "it", "ko", "pt"], // non-empty array of str
     "word_count": 71701829, // positive int
     "release_date": "2022-01-11T12:36:38+00:00" // null or ISO 8601 - always UTC
   }
   ```

   - Success sample response payload:

   ```json
   {
     "id": "312e8e30-7624-4923-a805-84562b07b738", // UUID4
     "name": "Diablo 112", // unique, not empty string
     "available_languages": ["en", "de", "ru", "it", "ko", "pt"], // non-empty array of str
     "word_count": 71701829, // positive int
     "release_date": "2022-01-11T12:36:38+00:00", // null or ISO 8601 - always UTC
     "created_at": "2021-01-11T12:36:38+00:02" // ISO 8601 - keeps client timezone
   }
   ```

   - For success and failure return appropriate status codes

2. `GET /api/v1/games`

   - Return a list of not deleted games sorted DESC by `release_date`
   - if `?sort_by=created_at` is passed a list is sorted DESC by `created_at` instead
   - Success sample response payload:

   ```json
   {
     "games": [
       {
         "id": "379d6e11-7024-1893-a209-84562b07b333", // UUID4
         "name": "Final Fantasy", // unique, not empty string
         "available_languages": ["en", "es", "de", "it", "fr", "ko"], // non-empty array of str
         "word_count": 82741003, // positive int
         "release_date": "2022-01-11T12:36:38+00:00", // null or ISO 8601 - always UTC
         "created_at": "2021-01-11T12:36:38+00:02" // ISO 8601 - keeps client timezone
       }
     ]
   }
   ```

3. `GET /api/v1/games/{game_id}`

   - Return a game if it exists and is not deleted
   - Success sample response payload:

   ```json
   {
     "id": "312e8e30-7624-4923-a805-84562b07b738", // UUID4
     "name": "Diablo 112", // unique, not empty string
     "available_languages": ["en", "de", "ru", "it", "ko", "pt"], // non-empty array of str
     "word_count": 10076811, // positive int
     "release_date": "2022-01-11T12:36:38+00:00", // null or ISO 8601 - always UTC
     "created_at": "2021-01-11T12:36:38+00:02" // ISO 8601 - keeps client timezone
   }
   ```

4. `PUT /api/v1/games/{game_id}`
   - Update a game if it exists and is not deleted
   - Success sample request payload:
   ```json
   {
     "id": "332e8e30-1624-4923-a805-94562b07b556", // UUID4
     "name": "Super Mario World", // unique, not empty string
     "available_languages": ["en", "es", "de", "it", "fr", "ko"], // non-empty array of str
     "word_count": 91701298, // positive int
     "release_date": "2022-01-11T12:36:38+00:00", // null or ISO 8601 - always UTC
     "created_at": "2021-01-11T12:36:38+00:02" // ISO 8601 - keeps client timezone
   }
   ```
   - Success sample response payload:
   ```json
   {
     "id": "332e8e30-1624-4923-a805-94562b07b556", // UUID4
     "name": "Super Mario World", // unique, not empty string
     "available_languages": ["en", "es", "de", "it", "fr", "ko"], // non-empty array of str
     "word_count": 91701298, // positive int
     "release_date": "2022-01-11T12:36:38+00:00", // null or ISO 8601 - always UTC
     "created_at": "2021-01-11T12:36:38+00:02" // ISO 8601 - keeps client timezone
   }
   ```
5. `DELETE /api/v1/games/{game_id}`
   - Soft delete a game
   - Return 204 for successful operation

## Frontend

### Requirements ✅

1. Create a React + Typescript web app.
2. Build the following sections (route-based sections):

   2.1. **Games list**: In this section all game projects should be listed for users. Create action is also included here.

   - Each game item should show its basic information, this means: `name`, `release_date` and `available_languages`.

   - The user should be able to create a new game project, for which a button should be available in the section and a modal opened for it with a form including all the data necessary to create the game. 🔥 _Bonus_: Update the list without refetching the all the games.

   - This section should be accessible by the url `/games`.

   ✨ _Hint:_ Use `GET /api/v1/games` endpoint fetch the games and `POST /api/v1/games` to create them.

   2.2. **Game details**: Section where all the information of a project is rendered. Users can edit and delete them here.

   - Render all the information of the game, this means: `name`, `created_at`, `release_date`, `word_count` and `available_languages`.

   - Each field should be editable. You can just add a general **Save** button for this. 🔥 _Bonus_: Add autosave on edit for each field and allow to update the UI without refetching the updated game.

   - There should be a _Delete_ button to delete the project. After deleting it, the user should be redirected to the updated list.

   - This section should be accessible by the url `/games/${gameId}`.

   ✨ _Hint:_ Use `GET /api/v1/games/{game_id}` endpoint fetch the game information, the `PUT /api/v1/games/{game_id}` to update it and the `DELETE /api/v1/games/{game_id}` to delete it.

3. Track and render loading states to user.
4. Test your code! With unit tests is enough for this challenge.
5. Style your app! We care about UI/UX :)

### Designs 🌄 (wireframes)

It is not necessary to stick a 100% to the wireframes. You can be creative!

- Games list section:

![alt text](https://altagram-public-image-hosting.s3.eu-central-1.amazonaws.com/fullstack-code-challenge-1.png)

![alt text](https://altagram-public-image-hosting.s3.eu-central-1.amazonaws.com/fullstack-code-challenge-2.png)

- Game details section:

![alt text](https://altagram-public-image-hosting.s3.eu-central-1.amazonaws.com/fullstack-code-challenge-3.png)

## Happy hack! 🚀
