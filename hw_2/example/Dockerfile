FROM continuumio/miniconda3

WORKDIR /app

RUN apt-get update -y && apt-get install -y texlive-latex-base
RUN conda update -n base -c defaults conda && \
    conda create -n latex_env python=3.12 && \
    conda clean --all --yes

RUN /bin/bash -c "source activate latex_env"
RUN conda install hackass2002::latex_generator

ENTRYPOINT [ "/bin/bash", "-c", "python3 . && pdflatex res.tex" ]
