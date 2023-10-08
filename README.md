# BATTLE OF MONSTERS

The app is called battle of monsters, where we have different monsters with different stats like attack and defense, for example, and we can let them fight each other. Is uses RESTful api that services requests for monsters and battles. Built using DRF.

## RULES:

- The monster with the highest speed makes the first attack, if both speeds are equal, the monster with the higher attack goes first.
- The damage is calculated by subtracting the defense from the attack (attack - defense); if the attack is equal to or lower than the defense, the damage is 1.
- The damage is subtracted from the HP (HP = HP - damage).
- Monsters will battle in turns until one wins; all turns are calculated in the same request; for that reason, the battle endpoint return winner data in just one call.
- Who wins the battle is the monster who subtracted the enemy’s HP to zero

## QUICKSTART

Create the Python venv

```bash
python -m venv venv
```bash

Install the dependencies

```bash
pip install -r requirements/requirements.txt
```

Database migrations and seeds

```bash
pip install -r requirements/requirements.txt
```

Run the app:

```bash
make runserver
```

Run the tests:

```bash
make test
```

Run the tests per module:

```bash
make test_module
```

Go to `http://localhost:8080` and the endpoints.

### ENDPOINTS

- '/monsters' -> Use CRUD operations to manage monsters items.
- '/batlles' -> Use CRUD operations to manage battles and see results.


## DEVELOPMENT NOTES:

Run the linter:

```bash
make lint
```

Fix most lint errors:

```bash
make test_module
```

The project includes 3 problem-solving module using python.