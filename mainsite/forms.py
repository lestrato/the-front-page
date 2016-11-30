from django import forms

class SubredditSearchForm(forms.Form):
    subreddit = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "required":True,
                "max_length":20,
                "class":"form-control input-sm",
                "placeholder":"subreddit name",
                "type":"text",
                # "display":"inline",
                # "id":"csInput",
            }
        ),
    )

    def clean(self):
        return self.cleaned_data
