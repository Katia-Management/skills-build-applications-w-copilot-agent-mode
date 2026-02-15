---
mode: agent
model: GPT-4.1
---

# Django App Updates

- All Django project files are in the `octofit-tracker/backend/octofit_tracker` directory.

1. Update `settings.py` for MongoDB connection and CORS.
2. Update `models.py`, `serializers.py`, `urls.py`, `views.py`, `tests.py`, and `admin.py` to support users, teams, activities, leaderboard, and workouts collections.
3. Ensure `/` points to the api and `api_root` is present in `urls.py`.

Tip: Use prompt files to define repeatable tasks and workflows.

When writing prompts focus on WHAT needs to be done. You can reference instructions for the HOW.

See the VS Code Docs: Prompt Files page for more information.
