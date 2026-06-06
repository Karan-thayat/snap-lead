from flask import Flask, render_template_string, request, redirect
import psycopg2

app = Flask(__name__)

# Database connection parameters
DB_PARAMS = {
    "dbname": "snaphomz", 
    "user": "karan", 
    "password": "password", 
    "host": "localhost"
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>SnapLead Approval Queue</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #f4f4f9; padding: 40px; color: #333; }
        .container { max-width: 800px; margin: auto; }
        .card { background: white; border-radius: 8px; padding: 24px; margin-bottom: 24px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .badge { background: #e2e8f0; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; font-weight: bold; }
        .content-box { background: #f8fafc; padding: 16px; border-left: 4px solid #3b82f6; margin: 16px 0; white-space: pre-wrap; font-family: monospace;}
        .btn { background: #10b981; color: white; border: none; padding: 10px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; }
        .btn:hover { background: #059669; }
    </style>
</head>
<body>
    <div class="container">
        <h1 style="border-bottom: 2px solid #ccc; padding-bottom: 10px;">SnapLead: AI Content Queue</h1>
        {% if not posts %}
            <p>All clear! No drafts pending review.</p>
        {% endif %}
        
        {% for post in posts %}
        <div class="card">
            <h2>{{ post[3] }}</h2>
            <p><span class="badge">Lead ID: {{ post[1] }}</span> <span class="badge">Keyword: {{ post[2] }}</span></p>
            <div class="content-box">{{ post[4] }}</div>
            <form action="/approve/{{ post[0] }}" method="POST">
                <button type="submit" class="btn">Approve & Ship to Blog</button>
            </form>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

def get_db_connection():
    return psycopg2.connect(**DB_PARAMS)

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM seo_content_queue WHERE review_status = 'pending'")
    posts = cur.fetchall()
    conn.close()
    return render_template_string(HTML_TEMPLATE, posts=posts)

@app.route('/approve/<int:content_id>', methods=['POST'])
def approve(content_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE seo_content_queue SET review_status = 'shipped' WHERE content_id = %s", (content_id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)