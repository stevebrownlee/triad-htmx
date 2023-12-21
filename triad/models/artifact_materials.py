from django.db import models

class ArtifactMaterials(models.Model):
    artifact = models.ForeignKey("Artifact", on_delete=models.CASCADE)
    material = models.ForeignKey("Material", on_delete=models.CASCADE)
    class Meta:
        unique_together = ('artifact', 'material')