#README for webhook-repo
GitHub Webhook Receiver
A Flask application that receives GitHub webhook events and displays them in a real-time UI.

Features
Receives GitHub webhook events (Push, Pull Request, Merge)
Stores events in MongoDB
Real-time UI with 15-second polling
Clean, responsive design
Event deduplication
Proper error handling
Setup Instructions
1. Clone the Repository
bash
git clone https://github.com/YOUR_USERNAME/webhook-repo.git
cd webhook-repo
2. Install Dependencies
bash
Flask
pymongo
flask-cors
python-dotenv
pip install -r requirements.txt
3. Configure Environment Variables
Create a .env file in the root directory:

MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/
FLASK_ENV=development
PORT=5000
4. Set Up MongoDB
Create a MongoDB Atlas account (free tier available)
Create a new cluster
Create a database named webhook_db
Get your connection string and add it to .env
5. Run the Application
bash
python app.py
6. Expose Your Local Server (For Testing)
bash
# Install ngrok
npm install -g ngrok

# In another terminal, expose your local server
ngrok http 5000
API Endpoints
GET / - Main UI page
POST /webhook - GitHub webhook endpoint
GET /api/events - Get recent events (JSON)

Project Structure
webhook-repo/
├── app.py              # Main Flask application
├─  requirements.txt    # Python dependencies
├── .env                # Environment variables    
├── .gitignore          # Git ignore rules            
├── templates/
│   └── index.html      # Main UI template
├── static/
     └── script.js      # Script File for events and function
     └──style.css       # Designing File
├── README.md           # This file

MongoDB Schema
json
{
  "_id": "ObjectId",
  "event_type": "push|pull_request|merge",
  "author": "string",
  "from_branch": "string",
  "to_branch": "string", 
  "timestamp": "ISO date string",
  }
Event Format Examples
Push Event
Format: {author} pushed to {to_branch} on {timestamp} Example: "Travis pushed to staging on 1st April 2021 - 9:30 PM UTC"

Pull Request Event
Format: {author} submitted a pull request from {from_branch} to {to_branch} on {timestamp} Example: "Travis submitted a pull request from staging to master on 1st April 2021 - 9:00 AM UTC"

Merge Event
Format: {author} merged branch {from_branch} to {to_branch} on {timestamp} Example: "Travis merged branch dev to master on 2nd April 2021 - 12:00 PM UTC"

Deployment
ngrok
Create a ngrok app
Set environment variables in ngrok dashboard
Start a tunnel in your terminal 
Deploy using Git:
bash
git add .
Connect your GitHub repository
Set environment variables
Deploy automatically
Testing
Configure GitHub webhook in your test repository
Make commits, create pull requests, and merge them
Check the UI at your deployed URL
Monitor logs for any errors
Troubleshooting
Common Issues
MongoDB Connection Error
Check your connection string
Ensure IP is whitelisted in MongoDB Atlas
Verify username/password
Webhook Not Receiving Events
Check webhook URL is correct
Verify webhook is configured for correct events
Check application logs
Events Not Displaying
Check browser console for errors
Verify API endpoint is working
Check MongoDB for stored events
Contributing
Fork the repository
Create a feature branch
Make your changes
Test thoroughly
Submit a pull request
README for action-repo
GitHub Action Repository
This is a dummy repository used to test GitHub webhook functionality. It triggers webhook events when:

Code is pushed to any branch
Pull requests are created
Pull requests are merged
Purpose
This repository serves as a test environment for the webhook receiver application. It contains sample code and multiple branches to simulate real development workflows.

Branches
main - Main development branch
staging - Staging environment
dev - Development branch
feature/* - Feature branches for testing
How to Test Webhook Events
1. Push Events
bash
# Clone this repository
git clone https://github.com/YOUR_USERNAME/action-repo.git
cd action-repo

# Make changes
echo "# Test change" >> test.txt
git add test.txt
git commit -m "Test webhook push event"
git push origin main
2. Pull Request Events
bash
# Create a new branch
git checkout -b feature/test-pr
echo "# PR test" >> pr_test.txt
git add pr_test.txt
git commit -m "Add PR test file"
git push origin feature/test-pr

# Create pull request through GitHub UI
3. Merge Events
Create a pull request (as above)
Review and merge the pull request through GitHub UI
This will trigger a merge webhook event
Files Description
src/main.py
python
def main():
    """Main application entry point"""
    print("Hello, GitHub Webhooks!")
    return "Success"

if __name__ == "__main__":
    main()
src/utils.py
python
def format_timestamp(timestamp):
    """Format timestamp for display"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validate_input(data):
    """Validate input data"""
    return data is not None and len(data) > 0
src/config.json
json
{
  "app_name": "GitHub Webhook Test App",
  "version": "1.0.0",
  "environment": "development"
}
Webhook Configuration
To connect this repository to your webhook receiver:

Go to Settings → Webhooks
Click Add webhook
Set Payload URL to: https://your-webhook-url.com/webhook
Set Content type to: application/json
Select Let me select individual events:
✅ Pushes
✅ Pull requests
Click Add webhook
Testing Checklist
 Repository webhook configured
 Push events trigger webhook
 Pull request creation triggers webhook
 Pull request merge triggers webhook
 Webhook receiver processes events correctly
 UI displays events in correct format
Notes
This is a test repository - code quality is not the focus
Feel free to create multiple branches for testing
Make frequent commits to generate webhook events
Use this repository to verify your webhook implementation works correctly

