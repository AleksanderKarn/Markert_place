# Market_place

Технические требования:

- Python 3.8+
- Django 3+
- DRF 3.10+
- PostgreSQL 10+

> реализована модель сети по продаже электроники.
> 
> иерархическую структуру состоит из 3 уровней:
- Завод
- Розничная сеть
- Индивидуальный предприниматель
> Реализован вывод в админ-панели созданных объектов;
> 
> На странице объекта сети добавлено:
- ссылку на «Поставщика»;
- фильтр по названию города;
- «admin action», очищающий задолженность перед поставщиком у выбранных объектов. 
> для модели поставщика (запрещено обновление через API поля «Задолженность перед поставщиком»);
> 
> добавлена возможность фильтрации объектов по определенной стране;
> 
>  Настроены права доступа к API так, чтобы только `активные` сотрудники имели доступ к API.