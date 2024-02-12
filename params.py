from model.utils import fix_len_compatibility


# data parameters
# train_filelist_path = 'fs2_txt/train.txt'
# valid_filelist_path = 'fs2_txt/valid.txt'
# test_filelist_path = 'fs2_txt/test.txt'

# train_filelist_path = 'file_list/speech_file_real/train.txt' 
# valid_filelist_path = 'file_list/speech_file_real/valid.txt'
# test_filelist_path = 'file_list/speech_file_real/test.txt'

# train_filelist_path = 'speech_file_real/train.txt' 
# valid_filelist_path = 'speech_file_real/valid.txt'
# test_filelist_path = 'speech_file_real/test.txt'

# "CoMoSpeech_VC/file_list/list_harsha"

train_filelist_path = 'file_list/list_harsha/train.txt' 
valid_filelist_path = 'file_list/list_harsha/valid.txt'
test_filelist_path = 'file_list/list_harsha/test.txt'


cmudict_path = 'resources/cmu_dictionary'
add_blank = True
n_feats = 80
n_spks = 1   
spk_emb_dim = 64
n_feats = 80
n_fft = 1024
sample_rate = 22050
hop_length = 256
win_length = 1024
f_min = 0
f_max = 8000

# encoder parameters
n_enc_channels = 192
filter_channels = 768
filter_channels_dp = 256
n_enc_layers = 6
enc_kernel = 3
enc_dropout = 0.1
n_heads = 2
window_size = 4

teacher = True # true for teacher model, false for consistency distillation

 
# training parameters
log_dir = 'logs/harsha_1' 
test_size = 2
n_epochs = 15000
batch_size =  8  
learning_rate = 1e-4
seed = 1234
save_every = 2000
out_size =  fix_len_compatibility(2*22050//256)