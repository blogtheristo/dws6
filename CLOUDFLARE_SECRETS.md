# Cloudflare GitHub Secrets - Ready to Add

## Add these 3 secrets to GitHub

Go to: **https://github.com/blogtheristo/dws6/settings/secrets/actions**

Click **"New repository secret"** for each:

---

### Secret 1: CLOUDFLARE_API_TOKEN
**Value:**
```
7apODsrHxfUvglqyYxqwVJo2501ZqTILJWIJv3zT
```

---

### Secret 2: CLOUDFLARE_ZONE_ID_DWS10
**Value:**
```
3d1ee683d9436a21b2211002f5a16832
```

---

### Secret 3: CLOUDFLARE_ZONE_ID_ONELIFETIME
**Value:**
```
409f65ed2f9a97e329acbfe3887a629b
```

---

## After Adding Secrets

Once you add these secrets:
1. ✅ The GitHub Actions workflow will automatically purge Cloudflare cache on every push
2. ✅ No more manual cache purging needed
3. ✅ Changes will appear within 30 seconds globally

## Test the Workflow

After adding secrets, make a small change and push:
```bash
git add .
git commit -m "Test Cloudflare cache purge"
git push origin main
```

Then check: https://github.com/blogtheristo/dws6/actions
You should see "Purge Cloudflare Cache" workflow running.

