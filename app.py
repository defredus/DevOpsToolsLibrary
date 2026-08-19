from flask import Flask, render_template

app = Flask(__name__)

showcases = [
    {
        "id": "01",
        "title": "CI / CD",
        "code": "PIPELINE.SYSTEM",
        "description": "Сборка, тестирование и доставка изменений в production.",
        "tools": ["GitLab CI", "GitHub Actions", "Jenkins", "Argo CD"],
    },
    {
        "id": "02",
        "title": "Orchestration",
        "code": "WORKLOAD.CONTROL",
        "description": "Управление сервисами, масштабированием и жизненным циклом приложений.",
        "tools": ["Kubernetes", "Helm", "Nomad", "OpenShift"],
    },
    {
        "id": "03",
        "title": "Containers",
        "code": "APPLICATION.PACKAGING",
        "description": "Изоляция, упаковка и запуск приложений в одинаковой среде.",
        "tools": ["Docker", "Podman", "Docker Compose", "Containerd"],
    },
    {
        "id": "04",
        "title": "Infrastructure as Code",
        "code": "INFRASTRUCTURE.DEFINED",
        "description": "Описание инфраструктуры в коде и её воспроизводимое развёртывание.",
        "tools": ["Terraform", "Ansible", "Pulumi", "Packer"],
    },
    {
        "id": "05",
        "title": "Observability",
        "code": "SYSTEM.VISIBILITY",
        "description": "Метрики, логи, трассировка и понимание состояния систем.",
        "tools": ["Prometheus", "Grafana", "Loki", "Jaeger"],
    },
    {
        "id": "06",
        "title": "Security",
        "code": "SECURE.DELIVERY",
        "description": "Защита секретов, образов, инфраструктуры и pipeline-процессов.",
        "tools": ["Vault", "Trivy", "Snyk", "Falco"],
    },
]

@app.route("/")
def index():
    return render_template("index.html", showcases=showcases)

if __name__ == "__main__":
    app.run(debug=True)