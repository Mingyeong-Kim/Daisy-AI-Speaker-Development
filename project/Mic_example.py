import speech_recognition as sr

def listen(self):
        """Listens to response from microphone and converts to text"""
        self.userCommand = ""
        with sr.Microphone(device_index=self.mic, chunk_size=1024, sample_rate=48000) as source:
            print ("\tThreshold: " + str(self.r.energy_threshold))
            print ("\tWaiting for words...")
            try:
                audio = self.r.listen(source, timeout=5)
                # self.playSound("end.mp3")
                try:
                    self.userCommand = self.r.recognize_google(audio)
                    self.userCommand = self.userCommand.lower()
                    if not self.processcommand(self.userCommand, source):
                        return False
                    else:
                        return True
                except sr.UnknownValueError:
                    print ("\t...")
                except sr.RequestError as e:
                    print("\tCould not request results from Google Speech Recognition service; {0}".format(e))
                except Exception as e:
                    print (str(e))
            except Exception:
                print ("\tNo audio heard")
                pass 