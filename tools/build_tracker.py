from datetime import date
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.formatting.rule import FormulaRule
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.properties import PageSetupProperties
from openpyxl.utils import get_column_letter as L

import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "2026_AI_FLEET_tracker.xlsx"
F = "Arial"
font = lambda **k: Font(name=F, size=k.pop("size", 10), **k)
fill = lambda c: PatternFill("solid", start_color=c, end_color=c)
thin = Side(style="thin", color="BFBFBF"); box = Border(left=thin, right=thin, top=thin, bottom=thin)
HEAD = fill("1F4E5F"); YEL = fill("FFF200")
cfill = {"MED":"D6E4EA","Engage":"F4D9BE","RPME":"F8D0D0","Transverse":"D7E8D4"}
d = lambda j, m: date(2026, m, j)
D_, IP, NS, BL, AC = "Done", "In progress", "Not started", "Blocked", "To confirm"
TBN = "To be named"
DOC = "PRD and technical document: writing, questions asked"
VAL = "PRD then technical document: validation"
cm_val = "Validation of the PRD (business) then the technical document. Ready within one week in total, build and test the following week"
BC = "Depends on the choice of the new model (T2)"
J_DOC = "Jordan writes, Arlette in support. 1 day to write and ask the questions (Arlette's value, to confirm with Jordan)"
A_DOC = "Arlette writes. 1 day to write and ask the questions (Arlette's value)"
P1 = "W1 Transmission plan (Jordan, Arlette in support)"
P3 = "W3 Valuation (Jordan, Arlette in support)"
P5 = "W5 Sales file"
P7 = "W7 Handover scenario"
PREP = "RPME: preparation (Jordan)"
FIRSTSHARE = "First share with the team on 27/10 (Arlette). "
rows = [
("M1","MED","MED global","Scoping","Arlette / Matthieu / Vero",D_,"",d(8,9),d(8,9),"",None,None),
("M2","MED","EcoVadis","First assessment: Audit Workflow User Experience document","Arlette",D_,"M1",d(17,9),d(18,9),"Blocked for a while by missing information on the MED side",None,None),
("M3","MED","MCP data","First assessment: MCP connected and shared","Vero",D_,"M1",None,d(8,10),"MCP available in production for Coptain Transition on 08/10 (Vero), connectors shared on 09/10. Registrations and active learners only give all-time and last-30-days figures: monthly and weekly pending development (21/10)",None,None),
("M4","MED","EcoVadis","Share findings and present the reference document","Arlette / Matthieu / Vero",D_,"M2",d(24,9),d(24,9),"",None,None),
("M5","MED","EcoVadis","Final version and validation of the reference document","Arlette",D_,"M4",d(25,9),d(12,10),"Last version shared on 02/10 with Gaëlle and Isabelle, feedback on 12/10, update of the rules requested",None,None),
("M6","MED","MED global","MED global context","Isabelle",D_,"M4",d(28,9),None,"Finalised (Arlette, 26/10). Owner changed from 'MED crew' to Isabelle, MED referent: to confirm",None,None),
("M7","MED","EcoVadis","Build the agent-specific context","Arlette",D_,"M5",d(29,9),d(15,10),"Workflow ready to test on staging on 15/10",None,None),
("M8","MED","EcoVadis","Ticket: input upload format","To be named",AC,"",None,None,"Mentioned in a comment of the original plan, attached to EcoVadis: to confirm. Status and owner to confirm",None,None),
("M9","MED","EcoVadis","Build the workflow: EcoVadis","Arlette",D_,"M7",d(2,10),d(15,10),"Ready to test on staging on 15/10. Sources differ on the shared version (v7-ton21 or v3 final)",None,None),
("M10","MED","EcoVadis","Test the workflow: EcoVadis","Arlette",D_,"M9",None,d(14,10),"Initial feedback was inconclusive. Test series of 13 to 14/10: M and XS validated",None,None),
("M11","MED","EcoVadis","Validate the workflow","Arlette / Matthieu / Vero",D_,"M10",None,d(14,10),"Decision of 14/10: shared version validated on M and XS",None,None),
("M12","MED","EcoVadis","Share V1 Beta","Arlette",D_,"M11",None,d(16,10),"Shared with the team for testing on staging",None,None),
("M13","MED","EcoVadis","V1 Beta feedback","Isabelle",D_,"M12",None,d(21,10),"Feedback of 21/10 did not help progress: rules and outputs were too limited. Matthieu asked Isabelle for more feedback the same day",None,None),
("M13b","MED","EcoVadis","Validation of the report mock-up and the question 'should an objective change the plan?'","Isabelle",NS,"M13",None,None,"Pending according to the MED tracker",None,None),
("M13c","MED","EcoVadis","Rework after the feedback: extend the rules and outputs","Arlette",AC,"M13",None,None,"Linked to the new LLM models (T2) and to the PRD and technical document method",None,None),
("M14","MED","EcoEntreprise","Agents reader, impact-analyst, classifier and gap-analyst validated","Arlette",D_,"",None,None,"Source: MED tracker",None,None),
("M15","MED","EcoEntreprise","Task-planner: v16 chain tested","Arlette",D_,"M14",None,d(21,10),"4 runs, 3 clean",None,None),
("M16","MED","EcoEntreprise","Writer: stabilise part 1","Arlette",IP,"M15",None,None,"Writer v1 tested on 21/10",None,None),
("M17","MED","EcoEntreprise","Connection to MED Missions","Arlette",NS,"M16",None,None,"",None,None),
("M18","MED","Self-assessment","Waiting for feedback from the MED side","Isabelle",NS,"",None,None,"The MED tracker says 'waiting for Gaëlle'. Isabelle is the MED referent",None,None),
("E1a","Engage","Quiz recap","Scoping","Matthieu",D_,"",d(1,10),d(1,10),"Scoping meeting held on 01/10",None,None),
("E1b","Engage","Miss Engage","Scoping","Matthieu",D_,"",d(1,10),d(1,10),"Scoping meeting held on 01/10",None,None),
("E2a","Engage","Quiz recap","First assessment: preliminary evaluation with the plugin","Arlette",D_,"E1a",None,d(9,10),"Éric's input received on 09/10. 4 to 6 agents for Engage, level 4. Start with the quiz recap",None,None),
("E2b","Engage","Miss Engage","First assessment: preliminary evaluation with the plugin","Arlette",D_,"E1b",None,d(9,10),"Éric's input received on 09/10. 4 to 6 agents for Engage, level 4. Welcome agent: one agent, two contexts",None,None),
("E3a","Engage","Quiz recap","Decision of 14/10: start with the quiz recap, ready for the SEEPH pilot","Arlette",D_,"E2a",None,d(14,10),"",None,None),
("E3b","Engage","Miss Engage","Decision of 14/10: a single chat agent for onboarding and late joiners, ready for the SEEPH pilot","Arlette",D_,"E2b",None,d(14,10),"Matthieu's vision",None,None),
("E4","Engage","Quiz recap","Validation document","Arlette",IP,"E3a",None,None,"Draft v6 on 26/10",None,None),
("E5","Engage","Miss Engage","PRD of the welcome agent","Arlette",IP,"E3b",None,None,"Draft v3 on 26/10",None,None),
("E6","Engage","Quiz recap","Decide: manual or automatic trigger, and who validates before publication","Arlette",NS,"E4",d(30,10),None,"Target: end of the week, to start the build on 02/11. To decide before sending to Vincent",None,None),
("E8a","Engage","Quiz recap","Data arrival from Typeform and the platform: Vincent's answer","Vincent",BL,"",d(30,10),None,"Target: end of the week, to start the build on 02/11. To confirm with Vincent. Blocking according to the evaluation of 09/10",None,None),
("E8b","Engage","Miss Engage","Can the chat read the participant's progress and the challenge figures: Vincent's answer","Vincent",BL,"",d(30,10),None,"Target: end of the week, to start the build on 02/11. To confirm with Vincent",None,None),
("E9a","Engage","Quiz recap","Respondent and team thresholds, organisation context","Éric",BL,"",None,None,"Values requested on 09/10",None,None),
("E9b","Engage","Miss Engage","Organisation context and thresholds","Éric",BL,"",None,None,"Values requested on 09/10",None,None),
("E10a","Engage","Quiz recap","Date of the SEEPH challenge","Matthieu",AC,"",None,None,"No date found",None,None),
("E10b","Engage","Miss Engage","Date of the SEEPH challenge","Matthieu",AC,"",None,None,"No date found",None,None),
("E11","Engage","Quiz recap",VAL,TBN,NS,"",d(27,10),None,FIRSTSHARE+cm_val,4,None),
("E12","Engage","Quiz recap","Build","Arlette",NS,"E11",d(3,11),None,BC+". Not before 03/11, one week after the documents are shared (Arlette)",2,1),
("E13","Engage","Quiz recap","Test","Arlette",NS,"E12",None,None,"",3,None),
("E14","Engage","Miss Engage",VAL,TBN,NS,"",d(27,10),None,FIRSTSHARE+cm_val,4,None),
("E15","Engage","Miss Engage","Build","Arlette",NS,"E14",d(3,11),None,BC+". Not before 03/11, one week after the documents are shared (Arlette)",2,1),
("E16","Engage","Miss Engage","Test","Arlette",NS,"E15",None,None,"",3,None),
("R0","RPME","W1 Transmission plan","Kick-off with Arlette and Matthieu","Jordan",D_,"",d(16,10),d(16,10),"Kick-off for the whole RPME project",None,None),
("R1","RPME","W1 Transmission plan","Reference material from Jordan","Jordan",IP,"",d(6,11),None,"First draft on 26/10. Date kept by Arlette on 26/10",None,None),
("R2","RPME","W1 Transmission plan","Tax expert: identify and contact","Jordan + expert",NS,"",d(23,10),None,"",None,None),
("R3","RPME","W1 Transmission plan","Environment set up: mission groups, segments, profile fields","Jordan / Vero",NS,"",d(30,10),None,"Needed by all four workflows",None,None),
("R4","RPME","W1 Transmission plan","PRD and technical document: writing, questions asked","Jordan",NS,"R1",None,None,"Jordan end to end, Arlette in support. 1 day to write and ask the questions (Arlette's value, to confirm with Jordan)",1,None),
("R5","RPME","W1 Transmission plan","PRD then technical document: validation",TBN,NS,"R4",None,None,cm_val,4,None),
("R6","RPME","W1 Transmission plan","Build","Jordan",NS,"R5",None,None,BC+". Jordan end to end, Arlette in support. Starting duration to confirm with Jordan",2,1),
("R7","RPME","W1 Transmission plan","Test","Jordan",NS,"R6",None,None,"Jordan tests, Arlette in support",3,None),
("R8","RPME","W1 Transmission plan","Pilot validation by Matthieu and Jacob","Matthieu / Jacob",NS,"R7",None,None,"Validation delay to be set",None,None),
("R9","RPME","W1 Transmission plan","Go-live","RPME team",NS,"",d(30,11),None,"Target: end of November",None,None),
("R10","RPME","W3 Valuation","Reference material from Jordan","Jordan",IP,"",d(6,11),None,"First draft on 26/10. Date kept by Arlette on 26/10",None,None),
("R11","RPME","W3 Valuation","Valuation expert: identify and contact","Jordan + expert",NS,"",d(23,10),None,"W4 (paid report) also needs the valuation multiples table, which does not exist",None,None),
("R12","RPME","W3 Valuation","PRD and technical document: writing, questions asked","Jordan",NS,"R10",None,None,"Jordan end to end, Arlette in support. 1 day to write and ask the questions (Arlette's value, to confirm with Jordan)",1,None),
("R13","RPME","W3 Valuation","PRD then technical document: validation",TBN,NS,"R12",None,None,cm_val,4,None),
("R14","RPME","W3 Valuation","Build","Jordan",NS,"R13",None,None,BC+". Jordan end to end, Arlette in support. Starting duration to confirm with Jordan",2,1),
("R15","RPME","W3 Valuation","Test","Jordan",NS,"R14",None,None,"Jordan tests, Arlette in support",3,None),
("R16","RPME","W3 Valuation","Pilot validation by Matthieu and Jacob","Matthieu / Jacob",NS,"R15",None,None,"Validation delay to be set",None,None),
("R17","RPME","W3 Valuation","Go-live","RPME team",NS,"",d(30,11),None,"Target: end of November",None,None),
("R18","RPME","W5 Sales file","Gather the existing document templates","Jordan",NS,"",d(16,10),None,"Jordan's date",None,None),
("R19","RPME","W5 Sales file","Reference material from Jordan","Jordan",NS,"",None,None,"First draft on 26/10. No date from Jordan. Matthieu must decide the output format (PowerPoint or Word) and the template",None,None),
("R20","RPME","W5 Sales file","PRD and technical document: writing, questions asked","Arlette",NS,"R8",None,None,"Starts once the two pilots are validated (Jordan's condition). Arlette writes. 1 day to write and ask the questions",1,None),
("R21","RPME","W5 Sales file","PRD then technical document: validation",TBN,NS,"R20",None,None,cm_val,4,None),
("R22","RPME","W5 Sales file","Build","Arlette",NS,"R21",None,None,BC,2,1),
("R23","RPME","W5 Sales file","Test","Arlette",NS,"R22",None,None,"",3,None),
("R24","RPME","W5 Sales file","Go-live","RPME team",NS,"",d(30,11),None,"Target: end of November",None,None),
("R25","RPME","W7 Handover scenario","Reference material from Jordan","Jordan",NS,"",None,None,"First draft on 26/10. No date from Jordan",None,None),
("R26","RPME","W7 Handover scenario","PRD and technical document: writing, questions asked","Arlette",NS,"R8",None,None,"Starts once the two pilots are validated (Jordan's condition). Arlette writes. 1 day to write and ask the questions",1,None),
("R27","RPME","W7 Handover scenario","PRD then technical document: validation",TBN,NS,"R26",None,None,cm_val,4,None),
("R28","RPME","W7 Handover scenario","Build","Arlette",NS,"R27",None,None,BC,2,1),
("R29","RPME","W7 Handover scenario","Test","Arlette",NS,"R28",None,None,"",3,None),
("R30","RPME","W7 Handover scenario","Go-live","RPME team",NS,"",d(30,11),None,"Target: end of November",None,None),
]
rows += [
("T1","Transverse","Agent builder plugin","Update the plugin","Arlette",D_,"",d(18,9),d(18,9),"",None,None),
("T2","Transverse","New LLM models","Choice of the new model: success criteria to validate, then shortlist test","Arlette",IP,"",None,None,"Applies to all clients. No run before validation. Waiting on Matthieu: data residency, budget, model route",None,None),
("T3","Transverse","Rework of some agents","Target of about 5 agents per workflow, once more powerful models are integrated","Arlette",NS,"T2",None,None,"Direction of 22/10: 23 agents for 2 workflows, not maintainable",None,None),
]
EXTRA = {"E12": ["E8a","E6"], "E15": ["E8b"], "R6": ["R3"], "R14": ["R3"], "R20": ["R16","R19"], "R26": ["R16","R25"]}
FIRST = 6; LAST = FIRST+len(rows)-1
projects = []
for r in rows:
    if (r[1], r[2]) not in projects: projects.append((r[1], r[2]))

wb = Workbook(); sm = wb.active; sm.title = "Summary"
pl = wb.create_sheet("Planning"); nt = wb.create_sheet("Notes")
for s_ in (sm, pl): s_.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)

# ---------- Notes ----------
nt["A1"] = "Notes"; nt["A1"].font = font(bold=True, size=14)
nt["A3"] = "Reference date (today)"; nt["B3"] = d(26,10)
nt["A4"] = "First Monday of the timeline"; nt["B4"] = d(7,9)
for r in (3,4): nt[f"A{r}"].font = font(); nt[f"B{r}"].number_format = "dd/mm/yyyy"; nt[f"B{r}"].font = font(color="0000FF", bold=True); nt[f"B{r}"].fill = YEL
REF = "Notes!$B$3"
notes = [
"One document: the Summary tab is calculated from the Planning tab. Edit the Planning only. If you add a project name in the Planning, add a row for it in the Summary.",
"Dates come from the project members: Arlette's original plan, Jordan's tracker (RPME), the MED and Engage trackers, test series. A missing date stays an empty (yellow) cell.",
"Durations are Arlette's starting values of 26/10: 2 working days of build, 3 working days of test. The PRD and technical document step takes 1 day of writing plus 4 days of validation, so it is ready within one week. Build and test follow the week after. Blue duration cells can be edited. The Agents column shows the planned number of agents (5 maximum per workflow) and does not drive any calculation.",
"Start (calc.): next working day after the end of the 'After' and 'Also after' lines for lines with a duration; otherwise the end of the 'After' line, or the due date. If one of these lines has no date, the line has no date. Public holidays are not taken into account.",
"Overdue (days) = days between the due date and the reference date for an open line, or between the due date and the actual end for a late finished line. RPME: no overdue is calculated. Arlette's count starts on 26/10, when she came back from training.",
"Builds depend on the choice of the new LLM model (line T2). It is written as a comment and does not move any date until the model has a date.",
"RPME: the projects are W1, W3, W5 and W7 only (nobody owns W2). Everything else (reference material, experts, environment, templates, go-live) is a step inside one of them. Arlette builds W5 and W7. Jordan does W1 and W3 end to end and Arlette is in support: those lines track what Jordan has to do. Jordan's own durations are to be confirmed with him.",
"MED: Isabelle is the MED referent. 'MED crew' of the original plan is replaced by Isabelle and Gaëlle is not responsible for anything: to confirm line by line.",
"Sources of truth: the project trackers (MED, Engage, RPME). This document is a view of them, regenerated on request.",
]
for i,t in enumerate(notes):
    c = nt.cell(row=6+i, column=1, value=t); c.font = font(); c.alignment = Alignment(wrap_text=True, vertical="top"); nt.row_dimensions[6+i].height = 46
r0 = 6+len(notes)+1
nt.cell(row=r0, column=1, value="Points to confirm").font = font(bold=True)
confirm = [
"EcoVadis: the MED tracker says the shared version is v7-ton21, the test series of 14/10 says v3 final. Which one is right?",
"Engage, 30/10 target for Vincent's answer and for the trigger decision: taken from 'this week'. To be confirmed with Vincent.",
"RPME W1 and W3: durations of Jordan's PRD, build and test are Arlette's starting values, to confirm with Jordan. Who validates the PRD and technical documents is still to be named.",
"No SEEPH 2026 challenge date was found. The EcoVadis reference file ECOVADIS.md was too large to be read: the EcoVadis state comes from the MED tracker and the test series.",
]
for i,t in enumerate(confirm):
    c = nt.cell(row=r0+1+i, column=1, value=t); c.font = font(); c.alignment = Alignment(wrap_text=True, vertical="top"); nt.row_dimensions[r0+1+i].height = 32
nt.column_dimensions["A"].width = 130; nt.column_dimensions["B"].width = 14

# ---------- Planning ----------
pl["A1"] = "2026 AI Fleet: planning"; pl["A1"].font = font(bold=True, size=14)
pl["A2"] = "Reference date:"; pl["A2"].font = font(italic=True)
pl["D2"] = f"={REF}"; pl["D2"].number_format = "dd/mm/yyyy"; pl["D2"].font = font(italic=True)
heads = ["ID","Client","Project","Step","Owner","Status","After","Also after","Also after","Duration (working days)","Agents","Start (calc.)","Due date","Actual end","Effective end (calc.)","Overdue (days)","Open overdue (calc.)","Comments"]
widths = [5,10,26,46,15,11,7,7,7,9,7,11,11,11,11,8,8,52]
centred = (7,8,9,10,11,12,13,14,15,16,17)
for i,(h,w) in enumerate(zip(heads,widths), start=1):
    c = pl.cell(row=5, column=i, value=h); c.font = font(bold=True,color="FFFFFF"); c.fill = HEAD
    c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center" if i in centred else "left"); pl.column_dimensions[L(i)].width = w
pl.row_dimensions[5].height = 38
A_, M_, N_, O_ = (f"${x}${FIRST}:${x}${LAST}" for x in "AMNO")
NW = 16; W0 = 19
for k in range(NW):
    col = W0+k; c = pl.cell(row=5, column=col)
    c.value = "=Notes!$B$4" if k == 0 else f"={L(col-1)}5+7"
    c.number_format = "dd/mm"; c.font = font(bold=True,color="FFFFFF",size=8); c.fill = HEAD
    c.alignment = Alignment(horizontal="center", vertical="center", text_rotation=90); pl.column_dimensions[L(col)].width = 4.4
for i, r in enumerate(rows):
    n = FIRST+i
    (id_,cl,pj,et,ow,st,af,due,done,co,du,ag) = r
    for j,v in zip(range(1,8),(id_,cl,pj,et,ow,st,af or None)): pl.cell(row=n, column=j, value=v)
    for k, x in enumerate(EXTRA.get(id_, [])): pl.cell(row=n, column=8+k, value=x)
    pl.cell(row=n, column=10, value=du); pl.cell(row=n, column=11, value=ag)
    pl.cell(row=n, column=14, value=done); pl.cell(row=n, column=18, value=co or None)
    pred = f'MATCH(G{n},{A_},0)'
    if du is not None:
        def pv(c): return f'IF({c}{n}="",0,IFERROR(INDEX({O_},MATCH({c}{n},{A_},0)),""))'
        cond = ",".join(f'AND({c}{n}<>"",NOT(ISNUMBER({pv(c)})))' for c in "GHI")
        has_pred = bool(af or EXTRA.get(id_))
        if due is not None and not has_pred:
            pl[f"L{n}"] = due
        else:
            core = f'WORKDAY(MAX({pv("G")},{pv("H")},{pv("I")}),1)'
            if due is not None: core = f'MAX(DATE({due.year},{due.month},{due.day}),{core})'
            pl[f"L{n}"] = f'=IFERROR(IF(OR({cond}),"",{core}),"")'
        pl[f"M{n}"] = f'=IF(L{n}="","",WORKDAY(L{n},J{n}-1))'
    else:
        pl[f"M{n}"] = due
        pl[f"L{n}"] = (f'=IF(O{n}="","",MIN(IF(M{n}<>"",M{n},O{n}),IF(G{n}="",O{n},IFERROR(IF(INDEX({N_},{pred})<>"",INDEX({N_},{pred}),'
                       f'IF(INDEX({M_},{pred})<>"",INDEX({M_},{pred}),O{n})),O{n}))))')
    pl[f"O{n}"] = f'=IF(N{n}<>"",N{n},IF(M{n}="","",IF(OR(F{n}="Done",B{n}="RPME"),M{n},MAX(M{n},{REF}))))'
    pl[f"P{n}"] = f'=IF(OR(B{n}="RPME",M{n}=""),"",IF(N{n}<>"",MAX(0,N{n}-M{n}),IF(F{n}="Done",0,MAX(0,{REF}-M{n}))))'
    pl[f"Q{n}"] = f'=IF(AND(ISNUMBER(P{n}),F{n}<>"Done"),P{n},"")'
    for col in range(1, W0+NW):
        c = pl.cell(row=n, column=col); c.font = font(); c.border = box
        c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center" if col in centred else "left")
        if col in (12,13,14,15): c.number_format = "dd/mm/yy"
    for col in (1,2,3): pl.cell(row=n, column=col).fill = fill(cfill[cl])
    if du is not None: pl.cell(row=n, column=10).font = font(color="0000FF", bold=True)
    for k in range(NW):
        col = W0+k; cl_ = L(col)
        c = pl.cell(row=n, column=col, value=f'=IF(OR($L{n}="",$O{n}=""),"",IF(AND($L{n}<={cl_}$5+6,$O{n}>={cl_}$5),1,""))')
        c.number_format = ";;;"
    pl.row_dimensions[n].height = 30
dv = DataValidation(type="list", formula1='"Not started,In progress,Done,Blocked,To confirm"', allow_blank=True)
pl.add_data_validation(dv); dv.add(f"F{FIRST}:F{LAST}")
rg = f"{L(W0)}{FIRST}:{L(W0+NW-1)}{LAST}"; tl = f"{L(W0)}{FIRST}"; hd = f"{L(W0)}$5"
pl.conditional_formatting.add(rg, FormulaRule(formula=[f'AND({tl}=1,$F{FIRST}="Done")'], fill=fill("A9D18E"), stopIfTrue=True))
pl.conditional_formatting.add(rg, FormulaRule(formula=[f'AND({tl}=1,ISNUMBER($Q{FIRST}),$Q{FIRST}>0)'], fill=fill("E57373"), stopIfTrue=True))
pl.conditional_formatting.add(rg, FormulaRule(formula=[f'AND({tl}=1,$F{FIRST}="In progress")'], fill=fill("9DC3E6"), stopIfTrue=True))
pl.conditional_formatting.add(rg, FormulaRule(formula=[f'{tl}=1'], fill=fill("BFBFBF"), stopIfTrue=True))
pl.conditional_formatting.add(rg, FormulaRule(formula=[f'AND($D$2>={hd},$D$2<={hd}+6)'], fill=fill("FFE699")))
pl.conditional_formatting.add(f"{L(W0)}5:{L(W0+NW-1)}5", FormulaRule(formula=[f'AND($D$2>={hd},$D$2<={hd}+6)'], fill=fill("BF8F00")))
pl.conditional_formatting.add(f"L{FIRST}:M{LAST}", FormulaRule(formula=[f'AND($L{FIRST}="",$F{FIRST}<>"Done")'], fill=YEL))
pl.conditional_formatting.add(f"P{FIRST}:P{LAST}", FormulaRule(formula=[f'AND(ISNUMBER($Q{FIRST}),$Q{FIRST}>0)'], font=Font(name=F,bold=True,color="C00000")))
pl.conditional_formatting.add(f"F{FIRST}:F{LAST}", FormulaRule(formula=[f'$F{FIRST}="Done"'], fill=fill("C6EFCE")))
pl.conditional_formatting.add(f"F{FIRST}:F{LAST}", FormulaRule(formula=[f'$F{FIRST}="In progress"'], fill=fill("DDEBF7")))
pl.conditional_formatting.add(f"F{FIRST}:F{LAST}", FormulaRule(formula=[f'OR($F{FIRST}="Blocked",$F{FIRST}="To confirm")'], fill=fill("FCE4D6")))
pl.column_dimensions["O"].hidden = True; pl.column_dimensions["Q"].hidden = True
pl.freeze_panes = "E6"; pl.auto_filter.ref = f"A5:R{LAST}"
pl.page_setup.orientation = "landscape"; pl.page_setup.fitToWidth = 1; pl.page_setup.fitToHeight = 0

# ---------- Summary (calculé depuis Planning) ----------
sm["A1"] = "2026 AI Fleet: summary by project"; sm["A1"].font = font(bold=True, size=14)
sm["A2"] = "Reference date:"; sm["A2"].font = font(italic=True)
sm["C2"] = f"={REF}"; sm["C2"].number_format = "dd/mm/yyyy"; sm["C2"].font = font(italic=True)
sh = ["Client","Project","Status","Steps","Done","In progress","Blocked / to confirm","Not started","Start","End","Open overdue (days)"]
sw = [11,46,12,7,7,9,10,9,11,11,10]
for i,(h,w) in enumerate(zip(sh,sw), start=1):
    c = sm.cell(row=4, column=i, value=h); c.font = font(bold=True,color="FFFFFF"); c.fill = HEAD
    c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center" if i >= 3 else "left"); sm.column_dimensions[L(i)].width = w
sm.row_dimensions[4].height = 38
SW0 = 12
for k in range(NW):
    col = SW0+k; c = sm.cell(row=4, column=col)
    c.value = "=Notes!$B$4" if k == 0 else f"={L(col-1)}4+7"
    c.number_format = "dd/mm"; c.font = font(bold=True,color="FFFFFF",size=8); c.fill = HEAD
    c.alignment = Alignment(horizontal="center", vertical="center", text_rotation=90); sm.column_dimensions[L(col)].width = 4.4
PC, PF, PL, PO, PQ = (f"Planning!${x}${FIRST}:${x}${LAST}" for x in "CFLOQ")
for i,(cl,pj) in enumerate(projects):
    n = 5+i
    sm.cell(row=n, column=1, value=cl).fill = fill(cfill[cl]); sm.cell(row=n, column=2, value=pj)
    sm[f"D{n}"] = f'=COUNTIFS({PC},$B{n})'
    sm[f"E{n}"] = f'=COUNTIFS({PC},$B{n},{PF},"Done")'
    sm[f"F{n}"] = f'=COUNTIFS({PC},$B{n},{PF},"In progress")'
    sm[f"G{n}"] = f'=COUNTIFS({PC},$B{n},{PF},"Blocked")+COUNTIFS({PC},$B{n},{PF},"To confirm")'
    sm[f"H{n}"] = f'=COUNTIFS({PC},$B{n},{PF},"Not started")'
    sm[f"C{n}"] = f'=IF(E{n}=D{n},"Done",IF(COUNTIFS({PC},$B{n},{PF},"Blocked")>0,"Blocked",IF(E{n}+F{n}>0,"In progress","Not started")))'
    sm[f"I{n}"] = f'=IF(COUNTIFS({PC},$B{n},{PL},">0")=0,"",_xlfn.MINIFS({PL},{PC},$B{n}))'
    sm[f"J{n}"] = f'=IF(COUNTIFS({PC},$B{n},{PO},">0")=0,"",_xlfn.MAXIFS({PO},{PC},$B{n}))'
    sm[f"K{n}"] = f'=IF(COUNTIFS({PC},$B{n},{PQ},">=0")=0,"",_xlfn.MAXIFS({PQ},{PC},$B{n}))'
    for col in range(1, SW0+NW):
        c = sm.cell(row=n, column=col); c.font = font(); c.border = box
        c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center" if col >= 3 else "left")
        if col in (9,10): c.number_format = "dd/mm/yy"
    for k in range(NW):
        col = SW0+k; cl_ = L(col)
        c = sm.cell(row=n, column=col, value=f'=IF(OR($I{n}="",$J{n}=""),"",IF(AND($I{n}<={cl_}$4+6,$J{n}>={cl_}$4),1,""))')
        c.number_format = ";;;"
    sm.row_dimensions[n].height = 22
SL = 4+len(projects)
for val, bg, fc in [("Done","C6EFCE","006100"),("In progress","BDD7EE","1F4E79"),("Blocked","F4B183","833C0B")]:
    sm.conditional_formatting.add(f"C5:C{SL}", FormulaRule(formula=[f'$C5="{val}"'], fill=fill(bg), font=Font(name=F, bold=True, color=fc)))
sm.conditional_formatting.add(f"K5:K{SL}", FormulaRule(formula=['AND(ISNUMBER($K5),$K5>0)'], font=Font(name=F,bold=True,color="C00000")))
srg = f"{L(SW0)}5:{L(SW0+NW-1)}{SL}"; stl = f"{L(SW0)}5"; shd = f"{L(SW0)}$4"
sm.conditional_formatting.add(srg, FormulaRule(formula=[f'AND({stl}=1,$C5="Done")'], fill=fill("A9D18E"), stopIfTrue=True))
sm.conditional_formatting.add(srg, FormulaRule(formula=[f'AND({stl}=1,ISNUMBER($K5),$K5>0)'], fill=fill("E57373"), stopIfTrue=True))
sm.conditional_formatting.add(srg, FormulaRule(formula=[f'AND({stl}=1,$C5="In progress")'], fill=fill("9DC3E6"), stopIfTrue=True))
sm.conditional_formatting.add(srg, FormulaRule(formula=[f'{stl}=1'], fill=fill("BFBFBF"), stopIfTrue=True))
sm.conditional_formatting.add(srg, FormulaRule(formula=[f'AND($C$2>={shd},$C$2<={shd}+6)'], fill=fill("FFE699")))
sm.conditional_formatting.add(f"{L(SW0)}4:{L(SW0+NW-1)}4", FormulaRule(formula=[f'AND($C$2>={shd},$C$2<={shd}+6)'], fill=fill("BF8F00")))
sm.freeze_panes = "C5"
sm.page_setup.orientation = "landscape"; sm.page_setup.fitToWidth = 1; sm.page_setup.fitToHeight = 0
wb.save(OUT); print("saved", len(rows), len(projects))
