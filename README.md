API системы задач в разработке.

Функционал:
* создавать отделы
* создавать должности в отделах
* добавлять сотрудников в отделы
* менеджеры могут создавать проекты и задачи в  рамка проекта, менять статус проектов (закрыт, отменен, в ожидании, в работе)
* задача "падает" сотруднику на почту, в письме приходит информация о задача и планируемом сроке ее выполнения
* сотрудник может создавать подзадачи для своей задачи, может менять ее статус (закрыта, отменена, в ожидании, в работе)
* рассчитывается активное и пассивное время работы над каждой задачей (например, если сотрудник зависим от подзадач и поставил ее на ожидание, а потом вернул в работу)
* статистика работы по отделам
* напоминания на почту когда срок задачи подходит к концу

Аутентификация по токенам благодаря Djoser. Для реализации возможности создавать подзадачи в рамках одной задачи Task-subTasks использована библиотека django-mptt.
Запросы должны содержать заголовок следующего вида: Authorization: Token "users token"
Напоминания о задачах и прочая рассылка redis+celery

| endpoint                 | description                                                                                                                                                                               | field                                                                                    | methods                 |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-------------------------|
| company/                 | Список департаментов (отделов)                                                                                                                                                            | name, description, url (to detail about department)                                      | GET, POST               |
| company/{id}/            | Информация об отделе, список названий должностей  (roles) и сотрудников (employees) в должностях  c краткой инфо о сотруднике и ссылкой "company/user/{id}" на профиль каждого сотрудника | name, description, roles(-employees short info)                                          | GET, PUT, PATCH, DELETE |
| company/{id}/roles/      | Список должностей с инфо о сотрудниках и ссылками на должности "company/roles/{id}"                                                                                                       | name, description, roles(-employees short info)                                          | GET, POST               |
| company/roles/{id}/      | Информация о должности                                                                                                                                                                    | name, description, roles(-employees short info)                                          | GET, PUT, PATCH, DELETE |
| company/users/{id}/      | Подробная информация о пользователе с ссылкой на должность "company/roles/{id}"                                                                                                           | first_name, last_name, email, birthday, gender, phone, role                              | GET, PUT, PATCH, DELETE |
| company/users/           | Список всех пользователей с краткой инфо                                                                                                                                                  | first_name, last_name, email, role, 'url'                                                | GET                     |
|                          |                                                                                                                                                                                           |                                                                                          |                         |
| task/projects/           | Список всех проектов, создание новых проектов если есть права менеджера                                                                                                                   | name, description, priority, planned_date, status, manager                               | GET, POST               |
| task/projects/{id}/      | Информация о проекте, о задачах в рамках проекта, возможность изменить статус (закрыть) проект, поставить на ожидание и тд.                                                               | name, description, priority, planned_date, status, manager, start_date, tasks[]          | GET, PUT, PATCH, DELETE |
| task/projects/{id}/tasks | Список задач в рамках проекта, создание задач, выбор исполнителя задачи                                                                                                                   | name, description, priority, planned_date, status, executor, start_date, project         | GET, POST               |
| task/{id}/               | Полная иформация о задаче, возможность сменить статус(закрыть, в ожидание), содержит ссылки на подзадачи и родительсике задачи task/{id} если они есть                                    | name, description, priority, planned_date, status, executor, start_date, project, parent | GET, PUT, PATCH, DELETE |
| task/{id}/delegate/      | Список подзадач, создание подзадачи                                                                                                                                                       | name, description, priority, planned_date, status, executor, start_date, project, parent | GET, POST               |
|                          |                                                                                                                                                                                           |                                                                                          |                         |
| auth/users/              | Регистрация нового пользователя                                                                                                                                                           | first_name, last_name, email, password                                                   | GET, POST               |
| auth/token/login/        | Получить токен для пользователя, если данные введены правильно - вернет "auth_token": "7...84"                                                                                            | email, password                                                                          | POST                    |
| auth/token/logout/       | Удалить токен пользователя                                                                                                                                                                | Заголовок: Authorization:  Token <your token>                                            | GET                     |
| auth/users/me/           | Узнать пользователя по токену                                                                                                                                                             | Заголовок: Authorization:  Token <your token>                                            | GET                     |
