# My Library

Personal Odoo learning project. This module revisits the concepts from the Vélotrace coursework through books and reading activity. It is not the school submission.

## Current version

The current module targets Odoo 18.0. The school project targets Odoo 19.0. Do not open the same database with both versions. Use `_sql_constraints` for this Odoo 18 module; use the appropriate Odoo 19 API in the school project.

## Local layout

```text
~/Me/Projets/
├── venv/
└── odoo/
    ├── odoo-bin
    ├── addons/
    └── custom-addons/  # this repository
        ├── README.md
        └── my_library/
```

These paths match the local setup used during the learning sessions. Adjust them if your environment changes.

## Start Odoo

Activate the existing environment:

```bash
source ~/Me/Projets/venv/bin/activate
cd ~/Me/Projets/odoo
```

Start an already installed module:

```bash
./odoo-bin --addons-path=addons,custom-addons -d odoo_demo
```

Update the module after changing models, views, security or data:

```bash
./odoo-bin --addons-path=addons,custom-addons -d odoo_demo -u my_library
```

For a first installation in a separate learning database:

```bash
./odoo-bin --addons-path=addons,custom-addons -d my_library_learning -i my_library
```

Open http://localhost:8069 and select the database used by your command. PostgreSQL must be running and accessible with your configured credentials. Stop the foreground server with Ctrl+C before starting another server on the same port.

## Common problems

- `./odoo-bin: No such file or directory`: run the command from `~/Me/Projets/odoo`, not from `custom-addons`.
- `No module named pytz`: check the active Python environment with `which python`; activate the existing venv before installing packages.
- Port 8069 already in use: stop the existing Odoo instance before launching another one.
- Changes missing: save your files, update the correct database with `-u my_library`, check the server log, then refresh the browser.
- Start from VS Code using the existing launch configuration only after checking its Python interpreter and database name.

## Existing learning topics

Book fields, categories with Many2one, cover images, list/form/search views, menus and window actions, access rights, ISBN constraints, state buttons and statusbar. Implementation and tests must be checked before considering any feature complete.

## Demo data cleanup

The current manifest lists `demo/demo_data.xml` in both `data` and `demo`. This should be reviewed: keep it only in `demo` if these records are optional demonstration data. This README does not modify the manifest.

## Next learning roadmap — planned, not implemented

### 1. Reading progress records — equivalent to GPS positions

Create `my_library.reading.progress` linked to a book. Store the page reached and a timestamp. Add a total page count to books. Validate page bounds. Users can read progress records but cannot create, modify or delete them directly. A dedicated wizard records progress for the current book. The book displays its latest progress and a smart button opens only its records, newest first.

Learning goals: One2many, TransientModel, context/defaults, access rights, safe controlled creation, computed fields and smart buttons.

### 2. Reading sessions — equivalent to rides

Create `my_library.reading.session` linked to a book, with progress records linked optionally to a session. Add points through a wizard. Compute start/end timestamps, duration in minutes and pages read from chronologically ordered records. Define and validate non-decreasing page numbers within a session before using last page minus first page. Isolated progress records remain valid without a session.

Learning goals: relational dependencies with `@api.depends`, stored computed fields, chronological ordering and validation. Haversine is specific to GPS and is not needed here.

### 3. Book counters — equivalent to ride counters

Show session count, total reading time and total pages read on the book. Add a Sessions tab and a smart button restricted to the current book. Totals come from session fields, not manually maintained values.

### 4. Reading badges — equivalent to distance badges

Create `my_library.badge` with name, description, positive page threshold and image. Configure badges through a Configuration menu. Assign eligible badges to a book with a button based on its total pages read. Repeated clicks must not create duplicates. Display earned badges on the book. Badges belong to books in this exercise, not yet to readers.

## Work method

Implement and explain one small step at a time. Test it before moving on. Do not generate the entire roadmap at once. Keep code and commit messages in English. Suggested feature branches: `feature/reading-progress`, `feature/reading-session`, `feature/reading-badges`.

Example commit:

```text
[ADD] my_library: add reading progress model
```

## Final checks

- Fresh database installation and module upgrade work.
- Invalid page values are rejected.
- Wizards know which book or session opened them.
- Direct progress edits are denied for normal internal users.
- Smart buttons show only related records.
- Adding progress updates dependent session and book totals.
- Repeated badge assignment creates no duplicates.
