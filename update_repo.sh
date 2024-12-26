# update_repo.sh

#!/bin/bash

# Shell script to update the "education-dashboard" GitHub repository

# Navigate to the project folder
# cd /path/to/education-dashboard

# Check the current status of the repository
echo "Checking the status of the repository..."
git status

# Add all changes to the staging area
echo "Adding changes to the staging area..."
git add .

# Commit the changes with a message
echo "Committing the changes..."
commit_message="Update project with latest changes on $(date)"
git commit -m "$commit_message"

# Push the changes to the main branch
echo "Pushing changes to GitHub..."
git push origin main

# Confirm the operation
echo "Repository updated successfully!"
