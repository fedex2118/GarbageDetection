# Trash detection & quantity estimation

This project was based on the analysis of Optimizing Waste Management with Advanced Object Detection for Garbage Classification by Everest Z. Kuang: https://arxiv.org/html/2410.09975v1.

This is the corresponding repository: https://github.com/everestkuang/GarbageDetectionYoloV5

# Structure

- The code for the two models is inside the two colab links.
- The real life test set used for inference is inside testSet
- The result of the inference is inside ModelsInference
- Inside inferenceStats there's stats.py which computes TPR and superflous boxes for the results
    - Beyond it there's also the various .txt we manually produced to identify the stats; this is the template: imageName_True/false performance for us_true/false performance for base study_excess boxes for us_excess images for base study
- The code to calculate the percentage occupied by trash inside the image is in computeArea.py
