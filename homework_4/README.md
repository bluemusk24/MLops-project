
### MLops Pipeline Project on Batch Processing (Offline Deployment)

* Notebook for this homework is <homework4.ipynb>

* The jupyter notebook was converted to a python script with the code below:

```bash
jupyter nbconvert --to script homework.ipynb
```

* The python script generated from the conversion is <homework4.py>

* Run this code below to get the mean of the duration prediction for April 2023:

```bash
python3 homework.py 2023 4
```

* To get the size of the output file:

```bash
ls -lh output_file/
```

* create a dockerfile:

```bash
touch dockerfile
```

* contents of dockefile below:

```bash
FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

RUN pip install -U pip
RUN pip install pipenv 

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["homework4.py", "./"]

CMD ["python", "homework4.py"]
```

* Build the docker image with this code below:

```bash
docker build -t batch:v1 .
```

* Run the container and the python script for May 2023 with these codes below:
```bash
docker run -it --rm --entrypoint=bash batch:v1

python3 homework4.py 2023 5
```

### Workflow Ochestration/execution with Mage AI Technology

* Run this code to start Mage AI container:

```bash
./scripts/start.sh
```

* Mage AI UI pictorial illustration for workflow orchestration of the <homework4.py> script:

![Refeference Image](Mage_1.png)

![Refeference Image](Mage_2.png)

![Refeference Image](Mage_3.png)

![Refeference Image](Mage_4.png)

![Refeference Image](Mage_5.png)

![Refeference Image](Mage_6.png)
