# devops Challenge 1

# docker
docker login --username highelf
docker build -t my-django-app .
docker tag my-django-app highelf/devops-challenge-1:latest
docker push highelf/devops-challenge-1:latest

docker run --name some-django-app -d -p 8000:8000 my-django-app

# kubernetes
kubectl apply -f k8s.yaml
kubectl port-forward svc/python-app 8080:8000