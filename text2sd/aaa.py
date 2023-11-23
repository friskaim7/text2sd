class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

def build_tree(lines):
    root = Node("Root")  # Root node with a placeholder value

    current_node = root
    stack = [root]

    for line in lines:
        # Ignore lines starting with ' or empty lines
        if not line.startswith("'") and line.strip():
            indent = line.count(' ')
            while len(stack) > indent + 1:
                stack.pop()

            new_node = Node(line.strip())
            stack[-1].children.append(new_node)
            stack.append(new_node)

    return root.children[0]  # Return the first child of the root as the actual root

# Your data sample
data_sample = '''
' 5
PreApplyLoansCmdExe.isWhiteListB(jsonData) >> Boolean:
    GoldFishManager.isWhiteListB(userId) >> boolean:
        UfiWhiteListDubboService.existsUfiWhiteList(userId) >> Boolean

' 6
PreApplyLoansCmdExe.process(jsonData) >> void:
    GoldFishManager.isGoldFish(loanNumber)>> boolean

' 7a
' 7b
GoldFishRule.FdcCheckHasOver15(userId, nik) >> Response<Boolean>:
    GoldFishRuleService.goldFishProcess(userType, loanNumber, userId, nik, StringBuilder) >> RuleResultDto:
        GoldFishRuleService.preReject(loanNumber) >> RuleResultDto:
            PreApplyLoansCmdExe.runPreRule(loanNumber) >> void:
                FdcFailJob.execute(shardingContext) >> void:

' 7d
FdcFailJob.execute(shardingContext) >> void
    PreApplyLoansCmdExe.runPreRule(loanNumber) >> void
        GoldFishRuleService.preReject(loanNumber) >> RuleResultDto
            GoldFishRule.ocrCheck(userId, sourceId) >> String
                ApplicationServiceFacde.getPaperworkDataList(userId, source) >> List<PaperworkDataVO>

' 7e
' 7f
' 7g
BaseRule.rejectByFNDI(userId) >> Boolean
    BaseRule.commonCheck(StringBuilder, applyInfoDto, loanNumber, item, mobile) >> RuleResultDto
        BaseRule.reject(loanNumber) >> RuleResultDto

' 7h
FifinsightController.getFifinsight()
    BaseFifinsightCheckService.getOneByNik(nik) >> FifinsightCheck
        FifInsightClient.loadFifinsightCheck(loadFifinsightCheck) >> FifinsightCheck
            GoldFishManager.fishFinderSecondCheck(ruleResultDto, loanNumber) >> RuleResultDto
                ApplyReportTwoConsumer.process(message) >> void

' 7i
BaseCheckService.gadaCheck(userInfo, loanNumber) >> String
    DukcapilClientV2Service.doCall(dukcapilRequest) >> String
        BaseCheckService.checkGadaAsli(loanNumber, docId) >> String
            BaseCheckService.checkBasicSelfie(VidaAsliBO ) >> String

' 7q
ScoreCheckService.getLastDigit(loanNumber) >> int
    BaseCheckService.getLastDigit()
        AbstractScoreCheckService.getApprovalScoreConfig(loanNumber, nik, userType) >> Response<ScoreResultBO>
            AbstractScoreCheckService.doResult(response, isScoreNullReject) >> Response<ScoreResultBO>
                ScoreCheck2GoldFish.doScoreCheck(nik, loanNumber) >> Response<ScoreResultBO>
                    ScoreCheck2GoldFish.checkScore(nik, loanNumber) >> Response<ScoreResultBO>
                        GoldFishManager.getCheckScore(userType, uw2aSegment, uw2bSegment, nik, loanNumber) >> Response<ScoreResultBO>
                            GoldFishManager.fishFinderSecondCheck(ruleResultDto, loanNumber) >> RuleResultDto
                               ApplyReportTwoConsumer.process(message) >> void

' 7r
GoldFishManager.getCreditTagUW2(origin, score, flagList) >> String
    BackstageConfigServiceFacade.getConfigValue(configKey) >> String

' 7s
ScoreCheck2GoldFish.scoreFive2Nine(nik, lastDigit, loanNumber) >> Response,
    ScoreCheck2GoldFish.defaultScoring(nik, lastDigit, loanNumber, userProfile) >> Respond

' 7u
BaseCheckService.checkSelfieScore(loanNumber) >> String:
    BaseCheckService.checkSelfieScoreNew(loanNumber, hitBasic) >> String:
        BaseCheckService.findKyc(loanNumber) >> String:
            BaseCheckService.vidaScoreCheck(loanNumber, hitBasic, type) >> Response<Boolean>:
                BaseCheckService.checkSelfieScoreVida(loanNumber, hitBasic, type) >> VerifyResultBO:
                    VidaClient.checkSelfieScore(loanNumber, hitBasic, type) >> VerifyResultBO:
                        VidaClient.checkLiveness(loanNumber, data) >> boolean:
                            VidaClient.checkCodesOrKycstatus(loanNumber, errors, data, respObj) >> boolean:
                                VidaClient.processCheckSelfieScore(loanNumber, errors, data, respObj) >> String
            BaseCheckService.verihubScoreCheck(loanNumber, hitBasic, type) >> Response<Boolean>:
                AsliClient.verifyAsliNew(loanNumber, hitBasic, type) >> String:
                    BaseCheckService.processCheckAsliScoreNew()

' 7v
' 7w
BaseCheckService.checkTeleStatus():
    BaseCheckService.checkAdvanceCallBack():
        BaseApprovalService.handAdvanceCallBack():
            AdvanceTeleConsumer.onMessage()

' 7x
NotifyUtils.saveTag()
'''

# Split the data into lines
lines = data_sample.split('\n')

# Build the tree
root = build_tree(lines)

def print_tree(node, indent=0):
    print(' ' * indent, node.data)
    for child in node.children:
        print_tree(child, indent + 4)

# Print the tree
print_tree(root)
