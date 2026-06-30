from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>DevSecOps Pipeline — AWS</h1>
    <p>This app was deployed automatically through a secure CI/CD pipeline.</p>
    <p>Pipeline: GitHub → CodePipeline → CodeBuild (security scan) → CodeDeploy → EC2</p>
    '''

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)