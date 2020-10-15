import pycorrector
from corrector import Corrector
import pandas as pd


def statistics(original_sentences, error_sentences, corrected_sentences):
    """用于统计精准率和召回率"""
    get_precision = lambda tp, fp : (tp * 1.0) / (tp + fp) # 获得准确率
    get_recall = lambda tp, tn : (tp * 1.0) / (tp + tn) # 获得召回率

    tp = 0
    fp = 0
    tn = 0

    for original_sentence, error_sentence, corrected_sentence in zip(original_sentences, error_sentences, corrected_sentences):
        if len(original_sentence) == len(error_sentence) and len(original_sentence) == len(corrected_sentence):
            for c1, c2, c3 in zip(original_sentence, error_sentence, corrected_sentence):
                if c1 == c3:
                    tp += 1
                if c1 != c3:
                    fp += 1
                if c1 == c2:
                    tn += 1

    print('precision \t{} \t recall \t{}'.format(get_precision(tp, fp), get_recall(tp, tn)))


def load_dataset(dataset_path):
    """加载数据集"""
    original_sentences = list() # 原句列表
    error_sentences = list() # 错句列表

    # 获取测试集
    with open(dataset_path) as f:
        for i, line in enumerate(f.readlines()):
            if i % 4 == 0:
                line = line.strip()[18:]
                original_sentences.append(line)
            elif i % 4 == 1:
                line = line.strip()[13:]
                error_sentences.append(line)
    
    return original_sentences, error_sentences


def process(error_sentences, kind):
    """纠正处理"""
    corrected_sentences = list()
    
    if kind == 'FMM':
        corrector = Corrector(kind)
    elif kind == 'BMM':
        corrector = Corrector(kind)
    elif kind == 'HMM':
        corrector = pycorrector
    
    for error_sentence in error_sentences:
        corrected_sentence = corrector.correct(error_sentence)[0]
        corrected_sentences.append(corrected_sentence)
    return corrected_sentences


def main():
    # dataset_path = './data/test.txt'
    # original_sentences, error_sentences = load_dataset(dataset_path)

    # kinds = ['FMM', 'BMM', 'HMM']

    # result = dict()

    # for kind in kinds:
    #     print("-----------{}-----------".format(kind))
    #     corrected_sentences = process(error_sentences, kind)
    #     result[kind] = corrected_sentences
    #     statistics(original_sentences, error_sentences, corrected_sentences)

    # with open('out.txt', 'a+') as f:
    #     for original, error, fmm, bmm, hmm in zip(original_sentences, error_sentences, result['FMM'], result['BMM'], result['HMM']):
    #         f.write('original\t{}\n'.format(original))
    #         f.write('error\t{}\n'.format(error))
    #         f.write('fmm\t{}\n'.format(fmm))
    #         f.write('bmm\t{}\n'.format(bmm))
    #         f.write('hmm\t{}\n\n'.format(hmm))

    
    # corrector = pycorrector
    # result = corrector.correct('我们来斗一斗音准')
    # print(result)
    
    corrector = Corrector('FMM')
    result = corrector.correct('我们来斗一斗音准')
    print(result)
    
            


if __name__ == "__main__":
    main()
