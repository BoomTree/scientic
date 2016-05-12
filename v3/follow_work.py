# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 15:48:30 2016

@author: Coco
"""

import forest
import db
from datetime import datetime



f = forest.forest()
f.setData('2007-1-21', 345)
f.normalize()
f.countSimilarity()
f.predict()


predict_plan = {"description": "test", i"datetime": datetime.today().strftime("%Y-%m-%d %H:%M:%S"), "predict_rate": f.predict_rate, "minRel": f.minRel, "predictNum": f.predictNum}
predict_plan_id = db.insertGetId("predict_plan", **predict_plan)
predict_plan["plan_id"] = predict_plan_id

for comparation in f.forestSimilarity:
    base = comparation.base
    base_info = {"pc_id": base.pc_id, "ah_id": base.ah_id, "predict_pc": base.powerConsume['predict'], "date": base.date}
    comparation_id = db.insertGetId("comparation", **base_info)
    for similarity in comparation.similarityEntitys:
        ap = similarity.ap
        ap_info = {"comparation_id": comparation_id, "pc_id": ap.pc_id, "ah_id": ap.ah_id, "similarity": similarity.similarity, "date": ap.date}
        db.insertGetId("similarity", **ap_info)


db.commit()
# print datetime.today().strftime("%Y-%m-%d %H:%M:%S")
