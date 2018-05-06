homo_dom = 27
hetero = 20
homo_rec = 21

total = homo_dom + hetero + homo_rec

prob_both_homo_dom = (float(homo_dom) / total) * (float(homo_dom-1)/(total-1))
print("DEBUG: Both homo dom: ", str(round(prob_both_homo_dom,6)))
prob_both_hetero = (float(hetero) / total) * (float(hetero-1)/(total-1))
print("DEBUG: Both hetero: ", str(round(prob_both_hetero,6)))
prob_both_homo_rec = (float(homo_rec) / total) * (float(homo_rec-1)/(total-1))
print("DEBUG: Both homo rec: ", str(round(prob_both_homo_rec,6)))
prob_homo_dom_and_hetero = (float(homo_dom) / total) * (float(hetero)/(total-1)) + (float(hetero) / total) * (float(homo_dom)/(total-1))
print("DEBUG: homo dom + hetero: ", str(round(prob_homo_dom_and_hetero,6)))
prob_homo_dom_and_homo_rec = (float(homo_dom) / total) * (float(homo_rec)/(total-1)) + (float(homo_rec) / total) * (float(homo_dom)/(total-1))
print("DEBUG: homo dom + homo rec: ", str(round(prob_homo_dom_and_homo_rec * 100,6)))
prob_homo_rec_and_hetero = (float(homo_rec) / total) * (float(hetero)/(total-1)) + (float(hetero) / total) * (float(homo_rec)/(total-1))
print("DEBUG: homo rec + hetero: ", str(round(prob_homo_rec_and_hetero,6)))

prob_dom_allele = prob_both_homo_dom * 1 + prob_homo_dom_and_hetero * 1 + prob_homo_dom_and_homo_rec * 1 + prob_both_homo_rec * 0 + prob_homo_rec_and_hetero * 0.5 + prob_both_hetero * 0.75
print(str(round(prob_dom_allele,6)))
